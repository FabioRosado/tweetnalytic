import tweepy

from config import CONSUMER_KEY, CONSUMER_SECRET
from config import ACCESS_TOKEN, ACCESS_SECRET

class SearchTwitter:
    """Searches twitter for last 1000 tweets about a term"""
    def __init__(self, term):
        self.term = term
        self._tweets = self._get_tweets()
        self._save_tweets()

    def _get_tweets(self):
        """Connect to twitter and search for term."""
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
        api = tweepy.API(auth)
        search = api.search(self.term, lang='en', count=100)

        print(f"Getting tweets that mention '{self.term}', "
              f"this may take a while...")

        save_tweet_text = [tweet._json['text'] for tweet in search]

        while len(save_tweet_text) < 1000:
            try:
                oldest = search[-1].id - 1
                search = api.search(self.term, lang='en', count=100, max_id=oldest)
                new_tweets = [tweet._json['text'] for tweet in search]
                save_tweet_text.extend(new_tweets)
            except IndexError:
                break

        print(f"Done. {len(save_tweet_text)} Tweets received.")
        return save_tweet_text

    def _save_tweets(self):
        file_path = f"./../tweets/{self.term}.txt"
        with open(file_path, 'w') as file:
            for tweet in self._tweets:
                file.write(f"'{tweet}' \n")

    def __len__(self):
        """Returns len of object - used to iterate over."""
        return len(self._tweets)

    def __getitem__(self, pos):
        """Get item in position - used to iterate over."""
        return self._tweets[pos]
