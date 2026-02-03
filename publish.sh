#!/bin/bash

# 1) UPDATE CONTENT
# Using rsync to mirror your Obsidian folder to the quartz content folder.
# --delete: removes files in quartz that you deleted in Obsidian.
# --exclude: skips hidden system files or obsidian configs.
SOURCE="/Users/fabian/Library/Mobile Documents/iCloud~md~obsidian/Documents/Computer Science/"
DEST="./content"

echo "Syncing content from Obsidian..."
rm -rf "$DEST"/* # Optional: Clear old content to ensure a clean slate, similar to 'create'
mkdir -p "$DEST"
cp -R "$SOURCE" "$DEST" 
# Note: cp -R is simpler; if you want exact mirroring (deleting removed files), use rsync:
# rsync -av --delete --exclude ".obsidian" --exclude ".git" --exclude ".DS_Store" "$SOURCE" "$DEST"

# 2) BUILD THE SITE
echo "Building Quartz site..."
npx quartz build

# 3) PUSH TO GITHUB
echo "Syncing to GitHub..."
npx quartz sync
