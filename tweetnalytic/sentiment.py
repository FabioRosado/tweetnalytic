import sys

from tweetnalytic.classifier import TweetsClassifier
from tweetnalytic.search import SearchTwitter
from collections import Counter


def classify_term(term):
    classifier = TweetsClassifier()
    try:
        with open(f'./../tweets/{term}.txt') as file:
            tweets = [tweet for tweet in file]
    except FileNotFoundError:
        tweets = [tweet for tweet in SearchTwitter(term)]

    scores = []

    for tweet in tweets:
        scores.append(classifier.classify(tweet))

    count = Counter(scores)
    try:
        print(f"Positive: {round(count['pos']/len(scores) * 100)}%")
        print(f"Negative: {round(count['neg']/len(scores) * 100)}%")
    except ZeroDivisionError:
        print(f"Sorry, no tweets received. Unable to rate '{term}'.")

print(classify_term("Renault"))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Unable to classify. No term specified')
        sys.exit(1)
    term = sys.argv[1]
    classify_term(term)

