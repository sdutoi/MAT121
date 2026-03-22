#!/bin/bash

rename_files() {
  for file in *; do
    if [[ -f "$file" ]]; then
      new_name=$(echo "$file" | sed \
        -e 's/ä/ae/g' \
        -e 's/ö/oe/g' \
        -e 's/ü/ue/g' \
        -e 's/Ä/Ae/g' \
        -e 's/Ö/Oe/g' \
        -e 's/Ü/Ue/g' \
        -e 's/ß/ss/g')
      
      if [[ "$file" != "$new_name" ]]; then
        mv "$file" "$new_name"
      fi
    fi
  done
}

rename_files
