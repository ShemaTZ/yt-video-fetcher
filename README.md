# YouTube Channel Video Metadata Extractor

This Python script fetches metadata for all videos from a specified YouTube channel using the YouTube Data API v3.

## Features

- Fetches video IDs, titles, descriptions, upload year & month.
- Automatically collects all videos from the channel (even if 100+ videos).
- Outputs data as a JSON file (`videos.json`).
- Sets the category field to "Bible" by default (can be customized it is Bible b/c I wanted it for my own purpose).

## Requirements

- Python 3.x
- `google-api-python-client` package

## Setup

1. Get a YouTube API key:
   - Go to [Google Cloud Console](https://console.developers.google.com/)
   - Enable **YouTube Data API v3**
   - Create an API key

2. Install required Python package:
   ```bash
   pip install google-api-python-client
