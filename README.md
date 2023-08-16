# YouTube Data Scraper

This is a Python script that uses the YouTube Data API to fetch data about videos based on a search parameter.

## Installation

1. Clone this repository.
2. Install the required packages using pip:

```bash
pip install -r requirements.txt
```

## Usage

Replace `"YOUR_API_KEY"` in `youtube_search.py` with your actual YouTube Data API key and `"search parameter"` with the actual search parameter.

Then, run the script:

```bash
python youtube_search.py
```

This will print the titles, views, likes, and comments of the top 10 videos that match the search parameter, sorted by the number of views.
