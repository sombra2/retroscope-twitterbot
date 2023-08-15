# Wikipedia On This Day Twitter Bot

This is a Python script that scrapes historical events from Wikipedia's "On This Day" page for tomorrow and posts them as tweets on Twitter using the Tweepy library.

## Overview

This script retrieves historical events from the Wikipedia page for tomorrow using web scraping techniques and then posts these events as tweets on Twitter. It's intended to be run periodically to keep the Twitter account updated with historical information.

## How it works

1. The script starts by scraping the Wikipedia page for "On This Day" events happening tomorrow.
2. It uses Beautiful Soup to parse the HTML content and extracts the relevant event information.
3. The extracted event information is then filtered using a regular expression to find events starting with a year.
4. The script authenticates with the Twitter API using the provided credentials.
5. The events are posted as tweets, with a random delay between each tweet.
6. The script sleeps for a certain period and then repeats the process.

## Prerequisites

- Python 3.x
- Required Python packages: tweepy, requests, beautifulsoup4
- Twitter developer account and Twitter API credentials

## Setup

1. Clone this repository.
2. Install the required packages using `pip install -r requirements.txt`.
3. Replace the `credentials.py` file with your actual Twitter API credentials.
4. Run the script using `python main.py`.

## Configuration

You can adjust the following parameters in the script:

- `url`: The Wikipedia URL for tomorrow's events.
- `random.randrange()` calls to adjust the timing of tweets.

## Twitter API Credentials

Make sure to set up your Twitter API credentials in the `credentials.py` file. Here's how the file should look:

```python
consumer_key = 'YOUR_CONSUMER_KEY'
consumer_secret = 'YOUR_CONSUMER_SECRET'
access_token = 'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'
bearer_token = 'YOUR_BEARER_TOKEN' # If using Twitter v2 API
