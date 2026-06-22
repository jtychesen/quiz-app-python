#!/bin/zsh

clear

cd "$(dirname "$0")" || {
    echo "Could not open quiz folder."
    echo ""
    read "?Press Enter to close..."
    exit 1
}

python3 main.py

echo ""
echo "Quiz finished."
read "?Press Enter to close..."