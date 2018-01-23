# Tweetnalytic

A simple program that uses the NLTK library to interact with Twitter. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

To run Tweetnalytic you need to install:

- NLTK
- Tweepy
- Oauthlib

### Installing

Install NLTK library and download all the data with the command:

```
sudo python -m nltk.downloader -d /usr/local/share/nltk_data all.
```
_Note: Read more on the [NLTK](http://www.nltk.org/data.html) page._

## Deployment

Simply run the following command in the command line:

```
python3 sentiment.py <term>
```

## Built With

* [NLTK](http://www.nltk.org/data.html) - Natural Language Toolkit
* [Tweepy](http://www.tweepy.org) - Tweepy: Twitter for Python!

## Authors

* **FabioRosado** - *Initial work* 

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

