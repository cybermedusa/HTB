#!/bin/bash

# Directory containing the files
directory="/path/to/your/directory"

# Change to the directory
cd "$directory"

# Loop through each file in the directory
for file in *; do
    # Check if it's a file and not a directory
    if [ -f "$file" ]; then
        # Create a zip file for each file
        zip "${file%.*}.zip" "$file"
    fi
done
