#!/bin/bash

if ! command -v python >/dev/null 2>&1; then
    echo "Python not found. Please install python to proceed."
    exit 1
fi

echo "Installing dependencies..."
python3 -m pip install -r requirements.txt