#!/bin/bash

directory="/path/to/your/directory"

cd "$directory"

for file in *; do
    if [ -f "$file" ]; then
        zip "${file}.zip" "$file"
    fi
done
