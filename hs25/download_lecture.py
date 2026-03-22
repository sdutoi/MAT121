#!/usr/bin/env python3
"""
Download SWITCHcast / Kaltura MediaSpace videos by pasting the media page URL.

Usage examples:
  - Paste a MediaSpace page URL:
      python3 download_lecture.py "https://uzh.mediaspace.cast.switch.ch/media/Analysis+I/0_6nbyov9t"

  - Optionally set output directory and custom name (without extension):
      python3 download_lecture.py URL --output-dir . --name "Analysis I HS25 - 2025-10-20"

  - If the media needs authentication, export cookies from your browser and pass them:
      python3 download_lecture.py URL --cookies /path/to/cookies.txt

Notes:
  - Requires `yt-dlp` to be installed (Homebrew: brew install yt-dlp). ffmpeg is optional
    but recommended (brew install ffmpeg).
  - By default, the script tries the constructed HLS manifest for Kaltura based on the
    page’s partnerId and entryId.
"""

import argparse
import os
import re
import sys
import shutil
import subprocess
from urllib.parse import urlparse
from urllib.request import Request, urlopen


def which(cmd: str) -> str | None:
    return shutil.which(cmd)


def fetch(url: str, headers: dict | None = None, timeout: int = 20) -> str:
    req = Request(url, headers=headers or {"User-Agent": "Mozilla/5.0"})
    with urlopen(req, timeout=timeout) as resp:
        data = resp.read()
    # Best-effort decoding
    try:
        return data.decode("utf-8", errors="ignore")
    except Exception:
        return data.decode("latin-1", errors="ignore")


def extract_first(pattern: str, text: str) -> str | None:
    m = re.search(pattern, text, flags=re.IGNORECASE | re.DOTALL)
    return m.group(1) if m else None


def parse_kaltura_info(page_html: str, fallback_domain: str | None = None):
    """Extract partnerId, entryId, serviceUrl host, and a good title if available."""
    # entryId usually appears in the player script as: loadMedia({entryId:"0_..."})
    # Support different quoting and spacing
    entry_id = extract_first(r"entryId\s*[:=]\s*['\"]([0-9A-Za-z_\-]+)['\"]", page_html)
    if not entry_id:
        entry_id = extract_first(r"entry_id[\s\"'=:\-]+([0-9A-Za-z_\-]+)", page_html)
    if not entry_id:
        # Links like /raw/entry_id/0_xxx/version/...
        entry_id = extract_first(r"/entry_id/([0-9A-Za-z_\-]+)/version", page_html)

    # partnerId appears in config: "partnerId":"106"
    partner_id = extract_first(r"\bpartnerId\b\s*[:=]\s*['\"](\d+)['\"]", page_html)

    # serviceUrl appears in config: "serviceUrl":"https://api.cast.switch.ch/api_v3"
    service_url = extract_first(r"\bserviceUrl\b\s*[:=]\s*['\"](https?://[^'\"]+)['\"]", page_html)
    service_host = None
    if service_url:
        p = urlparse(service_url)
        service_host = f"{p.scheme}://{p.netloc}"
    elif fallback_domain:
        service_host = fallback_domain

    # Try to get a nice title
    title = extract_first(r"<meta[^>]+property=['\"]og:title['\"][^>]+content=['\"]([^'\"]+)['\"]", page_html)
    if not title:
        title = extract_first(r"<title>([^<]+)</title>", page_html)

    return {
        "entry_id": entry_id,
        "partner_id": partner_id,
        "service_host": service_host,
        "title": (title or "Kaltura Video").strip(),
    }


def build_manifest_url(service_host: str, partner_id: str, entry_id: str, flavor_id: str = None) -> str:
    # Kaltura convention: sp is partnerId * 100 (as a string, usually looks like 10600 for partner 106)
    sp = f"{partner_id}00"
    
    if flavor_id:
        # Direct flavor URL (useful for selecting specific camera angle or quality)
        # Use the correct vod hostname for flavor URLs
        return f"https://vod.kaltura.switch.ch/hls/p/{partner_id}/sp/{sp}/serveFlavor/entryId/{entry_id}/v/2/ev/4/flavorId/{flavor_id}/name/a.mp4/index.m3u8"
    else:
        # Standard HLS manifest path (auto-selects quality)
        return f"{service_host}/p/{partner_id}/sp/{sp}/playManifest/entryId/{entry_id}/format/applehttp/protocol/https/a.m3u8"


def run_yt_dlp(
    source_url: str,
    out_path_tmpl: str,
    cookies: str | None = None,
    force_ffmpeg: bool = True,
    dry_run: bool = False,
) -> int:
    ytdlp = which("yt-dlp")
    if not ytdlp:
        print("Error: yt-dlp not found in PATH. Please install it, e.g.: brew install yt-dlp", file=sys.stderr)
        return 127

    cmd = [ytdlp, "-o", out_path_tmpl, "-N", "8", "--merge-output-format", "mp4"]

    if dry_run:
        cmd.append("-s")  # simulate

    cmd.append(source_url)

    # Prefer ffmpeg downloader for HLS if available
    if force_ffmpeg and which("ffmpeg"):
        cmd.extend(["--downloader", "ffmpeg", "--hls-use-mpegts"])  # better for HLS streams

    if cookies:
        cmd.extend(["--cookies", cookies])

    print("Running:", " ".join(cmd))
    rc = subprocess.call(cmd)
    
    # If download was successful, convert MPEG-TS to proper MP4 for better compatibility
    if rc == 0 and not dry_run and which("ffmpeg"):
        # Extract the actual output filename by checking what file was created
        output_dir = os.path.dirname(out_path_tmpl) or "."
        base_pattern = os.path.basename(out_path_tmpl).replace(".%(ext)s", "")
        
        # Look for the downloaded file
        for filename in os.listdir(output_dir):
            if filename.startswith(base_pattern) and filename.endswith(".mp4"):
                filepath = os.path.join(output_dir, filename)
                temp_filepath = filepath.replace(".mp4", "_temp.mp4")
                
                print(f"Converting {filename} to proper MP4 format for better compatibility...")
                convert_cmd = ["ffmpeg", "-i", filepath, "-c", "copy", "-y", temp_filepath]
                convert_rc = subprocess.call(convert_cmd)
                
                if convert_rc == 0:
                    # Replace original with converted version
                    os.replace(temp_filepath, filepath)
                    print(f"Successfully converted {filename} to standard MP4 format")
                else:
                    # Clean up temp file if conversion failed
                    if os.path.exists(temp_filepath):
                        os.remove(temp_filepath)
                    print(f"Warning: Could not convert {filename} to standard MP4 format")
                break
    
    return rc


def main():
    parser = argparse.ArgumentParser(description="Download Kaltura MediaSpace (SWITCHcast) videos via yt-dlp.")
    parser.add_argument("url", help="Media page URL (or direct .m3u8 URL)")
    parser.add_argument("--output-dir", "-o", default=".", help="Directory to save the video (default: current directory)")
    parser.add_argument("--name", "-n", default=None, help="Custom output filename without extension (default: derived from title and entry id)")
    parser.add_argument("--cookies", default=None, help="Path to cookies.txt (Netscape format) if authentication is required")
    parser.add_argument("--flavor-id", default=None, help="Specific Kaltura flavor ID to download (useful for selecting camera angle)")
    parser.add_argument("--screen-view", action="store_true", help="Try to download screen/presentation view (uses lower resolution flavor)")
    parser.add_argument("--force", action="store_true", help="Force re-download even if the output file exists")
    parser.add_argument("--dry-run", action="store_true", help="Simulate the yt-dlp run without downloading (passes -s)")

    args = parser.parse_args()
    os.makedirs(args.output_dir, exist_ok=True)

    url = args.url.strip()
    is_m3u8 = url.lower().endswith(".m3u8")

    # If user passed a direct HLS manifest, use it as-is.
    entry_id = None
    partner_id = None
    title = None
    manifest_url = url if is_m3u8 else None
    service_host = None

    if not is_m3u8:
        print("Fetching media page and extracting Kaltura parameters…")
        html = fetch(url)
        # Attempt to infer the fallback domain for service_host from known instances
        fallback_domain = None
        if "uzh.mediaspace.cast.switch.ch" in url:
            fallback_domain = "https://api.cast.switch.ch"

        info = parse_kaltura_info(html, fallback_domain=fallback_domain)
        entry_id = info.get("entry_id")
        partner_id = info.get("partner_id")
        service_host = info.get("service_host")
        title = info.get("title")

        # Fallbacks for known UZH MediaSpace pages if parsing fails
        if not entry_id:
            # try to pull id from the URL tail
            tail = extract_first(r"/([0-9A-Za-z_\-]+)/?(?:[#?].*)?$", url)
            if tail:
                entry_id = tail
        if not partner_id and "uzh.mediaspace.cast.switch.ch" in url:
            partner_id = "106"
        if not service_host and fallback_domain:
            service_host = fallback_domain

        if not entry_id or not partner_id or not service_host:
            print("Could not parse required Kaltura info (entryId/partnerId/service host).", file=sys.stderr)
            print("Try passing a direct .m3u8 URL or provide cookies if the page requires authentication.", file=sys.stderr)
            sys.exit(2)

        # Determine flavor ID to use
        flavor_id = args.flavor_id
        if args.screen_view and not flavor_id:
            # Use the lower resolution flavor which shows the digital screen/notes content
            flavor_id = "0_rkyu748z"  # Screen capture at 640x360 - shows digital notes/screen content
            print(f"Using screen view flavor: {flavor_id}")

        manifest_url = build_manifest_url(service_host, partner_id, entry_id, flavor_id)
        print(f"Discovered entryId={entry_id}, partnerId={partner_id}")
        if flavor_id:
            print(f"Using specific flavor: {flavor_id}")
        print(f"Using manifest: {manifest_url}")
    else:
        title = "Kaltura Video"

    # Output filename
    if args.name:
        base_name = args.name
    else:
        # Include entry_id to avoid collisions between similarly titled lectures
        suffix = f" ({entry_id})" if entry_id else ""
        base_name = f"{title}{suffix}".strip()

    # yt-dlp will choose the extension. We set a template to land in output_dir.
    out_tmpl = os.path.join(args.output_dir, f"{base_name}.%(ext)s")

    # If a file with .mp4 already exists and not forced, skip
    possible_mp4 = os.path.join(args.output_dir, f"{base_name}.mp4")
    if os.path.exists(possible_mp4) and not args.force:
        print(f"Already exists, skipping: {possible_mp4}")
        return 0

    rc = run_yt_dlp(
        manifest_url,
        out_tmpl,
        cookies=args.cookies,
        dry_run=args.dry_run,
    )
    if rc != 0:
        print("yt-dlp failed with exit code", rc, file=sys.stderr)
        # Guidance if authentication might be needed
        print("If this media requires authentication, export your browser cookies to cookies.txt and retry with --cookies PATH.", file=sys.stderr)
    return rc


if __name__ == "__main__":
    sys.exit(main())
