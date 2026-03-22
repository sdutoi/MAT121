#!/usr/bin/env bash
shopt -s nullglob

for f in *.tex; do
  [[ "$f" == hs24_*.tex ]] && continue
  tgt="hs24_$f"
  if [[ -e "$tgt" ]]; then
    echo "Skipping '$f' (target '$tgt' exists)" >&2
    continue
  fi
  echo "Renaming '$f' -> '$tgt'"
  mv -- "$f" "$tgt"
done