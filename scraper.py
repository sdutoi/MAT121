#!/usr/bin/env python3
"""
Scraper to download all übungsblätter and musterlösungen from UZH Math Analysis I course
URL: https://www.math.uzh.ch/ve-vo-det?key1=0&key2=4802&key3=469&semId=47
"""

import requests
from bs4 import BeautifulSoup
import os
import re
import time
from urllib.parse import urljoin, urlparse
import logging

# Setup logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


class UZHMathScraper:
    def __init__(
        self,
        base_url="https://www.math.uzh.ch/ve-vo-det?key1=0&key2=4445&key3=469&semId=43",
    ):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update(
            {
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
            }
        )
        self.download_dir = "downloads"

    def create_download_directory(self):
        """Create download directory if it doesn't exist"""
        if not os.path.exists(self.download_dir):
            os.makedirs(self.download_dir)
            logger.info(f"Created download directory: {self.download_dir}")

    def get_page_content(self):
        """Fetch the main page content"""
        try:
            response = self.session.get(self.base_url)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            logger.error(f"Error fetching page: {e}")
            return None

    def extract_download_links(self, html_content):
        """Extract all download links from the page"""
        soup = BeautifulSoup(html_content, "html.parser")
        download_links = []

        # Find all links that contain download.php (the download endpoint)
        links = soup.find_all("a", href=lambda href: href and "download.php" in href)

        for link in links:
            href = link.get("href")
            text = link.get_text(strip=True)

            # Convert relative URLs to absolute URLs
            if href.startswith("/"):
                href = f"https://www.math.uzh.ch{href}"
            elif not href.startswith("http"):
                href = urljoin(self.base_url, href)

            download_links.append(
                {
                    "url": href,
                    "text": text,
                    "filename": self.generate_filename(text, href),
                }
            )

        return download_links

    def generate_filename(self, link_text, url):
        """Generate a safe filename from link text"""
        # Clean up the link text to create a safe filename
        filename = re.sub(r"[^\w\s-]", "", link_text)
        filename = re.sub(r"[-\s]+", "_", filename)
        filename = filename.strip("_")

        # If filename is empty or too short, use URL parameter
        if len(filename) < 3:
            url_parts = urlparse(url)
            query_params = url_parts.query
            if "s=" in query_params:
                s_param = query_params.split("s=")[1].split("&")[0]
                filename = f"file_{s_param}"

        # Add .pdf extension if not present (most files are likely PDFs)
        if not filename.lower().endswith(".pdf"):
            filename += ".pdf"

        return filename

    def download_file(self, url, filename):
        """Download a single file"""
        filepath = os.path.join(self.download_dir, filename)

        # Skip if file already exists
        if os.path.exists(filepath):
            logger.info(f"File already exists, skipping: {filename}")
            return True

        try:
            logger.info(f"Downloading: {filename}")
            response = self.session.get(url, stream=True)
            response.raise_for_status()

            # Check if the response contains actual file content
            content_type = response.headers.get("content-type", "")
            if "text/html" in content_type:
                logger.warning(
                    f"Received HTML instead of file for {filename}, might be an error page"
                )
                return False

            with open(filepath, "wb") as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)

            file_size = os.path.getsize(filepath)
            logger.info(f"Successfully downloaded: {filename} ({file_size} bytes)")
            return True

        except requests.RequestException as e:
            logger.error(f"Error downloading {filename}: {e}")
            return False
        except IOError as e:
            logger.error(f"Error saving {filename}: {e}")
            return False

    def download_all(self):
        """Main method to download all files"""
        logger.info("Starting UZH Math Analysis I scraper...")

        # Create download directory
        self.create_download_directory()

        # Get page content
        html_content = self.get_page_content()
        if not html_content:
            logger.error("Failed to fetch page content")
            return

        # Extract download links
        download_links = self.extract_download_links(html_content)

        if not download_links:
            logger.warning("No download links found")
            return

        logger.info(f"Found {len(download_links)} download links")

        # Download each file
        successful_downloads = 0
        for i, link_info in enumerate(download_links, 1):
            logger.info(f"Processing {i}/{len(download_links)}: {link_info['text']}")

            if self.download_file(link_info["url"], link_info["filename"]):
                successful_downloads += 1

            # Add a small delay between downloads to be respectful
            if i < len(download_links):
                time.sleep(1)

        logger.info(
            f"Download complete! Successfully downloaded {successful_downloads}/{len(download_links)} files"
        )
        logger.info(f"Files saved to: {os.path.abspath(self.download_dir)}")


def main():
    scraper = UZHMathScraper()
    scraper.download_all()


if __name__ == "__main__":
    main()
