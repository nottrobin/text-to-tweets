# Tweetsplitter

This small package simply splits a large block of text into 280 character chunks.

The code is lifted wholesale from https://github.com/NaruBeast/tweet-splitter.

## Install

``` bash
pip3 install tweetsplitter
```

## Usage

``` python3
from tweetsplitter import tweet_splitter

tweets = tweet_splitter(
    article_text,
    counter=True  # Add counters to tweets - e.g. "(3/10)"
)
```
