#!/bin/bash

for file in ./contacts/*
do
    name=$(echo $file | cut -d '/' -f 3 | cut -d '.' -f 1)
    ./venv/bin/python3 upload-photo.py "$name" "$file"
    sleep 10
done
