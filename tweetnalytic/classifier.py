"""Class created from """
import nltk
import re
import pickle

from nltk.classify import NaiveBayesClassifier
from nltk.classify import accuracy
from nltk.corpus import stopwords
from nltk.tokenize import TweetTokenizer


class TweetsClassifier:
    """Used to transform, classify and return classification from sentence """
    def __init__(self):
        try:
            print("Loading classifier...")
            self.classifier = self.load_classifier()
            print(f"Classifier loaded...")
        except FileNotFoundError:
            self.classifier = self._train_classifier()

    def format_sentence(self, sent):
        """Tokenize sentence and return format that can work with
        NLTK.NaiveBayesClassifier."""
        RT_USERS_PUNC = re.compile(r'@\w+|\W|RT')

        tokenizer = TweetTokenizer()
        sent = tokenizer.tokenize(sent)
        sent = [token for token in sent if not RT_USERS_PUNC.search(token)]
        sent = [word for word in sent if word not in stopwords.words('english')]
        sent = ' '.join(sent)

        return {word: True for word in nltk.word_tokenize(sent)}

    def _get_positive_tweets(self):
        """Use different sources to get positive tweets and increase accuracy
        of the classifier."""
        print("Getting data: positive tweets...")
        positive_tweets = []
        with open('./../data/positive_tweets.txt') as file:
            for tweet in file:
                positive_tweets.append([self.format_sentence(tweet), 'pos'])
                if len(positive_tweets) == 2250:
                    print("Processed 2,250 Tweets so far - Halfway point reached")
        print(f"Done. {len(positive_tweets)} tweets collected")
        return positive_tweets

    def _get_negative_tweets(self):
        """Use different sources to get negative tweets and increase accuracy
        of the classifier."""
        negative_tweets = []
        print("Getting Data: negative tweets...")
        with open('./../data/negative_tweets.txt') as file:
            for tweet in file:
                negative_tweets.append([self.format_sentence(tweet), 'neg'])
                if len(negative_tweets) == 2250:
                    print("Processed 2,250 Tweets so far - Halfway point reached")
        print(f"Done. {len(negative_tweets)} tweets collected")
        return negative_tweets

    def _train_classifier(self):
        """Use 80% of tweets to train a classifier."""
        pos_tweets = self._get_positive_tweets()
        neg_tweets = self._get_negative_tweets()

        training = pos_tweets[:int(.8 * len(pos_tweets))] + \
            neg_tweets[:int(.8 * len(neg_tweets))]

        testing = pos_tweets[int(.8 * len(pos_tweets)):] + \
            neg_tweets[int(.8 * len(neg_tweets)):]

        print("Training Classifier...")

        classifier = NaiveBayesClassifier.train(training)
        print(f"Classifier trained with "
              f"success - accuracy rating: {round(accuracy(classifier, testing), 2)}%")

        self.save_classifier(classifier)
        return classifier

    def classify(self, text):
        """Uses trained classifier to classify a piece of text."""
        return self.classifier.classify(self.format_sentence(text))

    def save_classifier(self, classifier):
        with open('classifier.pickle', 'wb') as save_classifier:
            pickle.dump(classifier, save_classifier)

    def load_classifier(self):
        with open("classifier.pickle", "rb") as loaded_classifier:
            return pickle.load(loaded_classifier)
