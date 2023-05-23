#region Description: task3
print('input is: translated_tweet')
#############################################################################################################
mwe_words = [('hamoon', 'lake'), ('sistan', 'region'), ('sistan', 'and', 'baluchestan'), ('24', 'hours'),('kamal','khan')]
#print(len(translated_tweet))
#############################################################################################################
import tweepy

import nltk
# nltk.download() #use it of you need book text sample

from nltk.tokenize import TweetTokenizer
from nltk.tokenize import MWETokenizer
from nltk.probability import FreqDist
from nltk.corpus import stopwords
import itertools
import matplotlib

# here we tokenize
tk = MWETokenizer(mwe_words)
tokenized_tweets = []
for tweet in translated_tweet:
    tweet = tweet.lower()
    tokenized = tk.tokenize(tweet.split())
    tokenized_tweets.append(tokenized)

# print(tokenized_tweets)

# here we delete stopwords:
# print(stopwords.words('english'))
stop_words = set(stopwords.words('english'))

filtered_tweets = []
for tweet in tokenized_tweets:
    filtered = [w for w in tweet if not w in stop_words]
    filtered_tweets.append(filtered)
# print(filtered_tweets)

type(filtered_tweets) #each parameter of this list is a seperate list but all of them should be unified list so we flaten it:
chain_object = itertools.chain.from_iterable(filtered_tweets)
flattened_tweets = list(chain_object)
#print(flattened_tweets) #now our tweets data set is a unified list

#here we correct some misspellings because of translated by google translation:
wrong_spell = ("zabol","zaboul","hamoun","hamon")
correct_spell = ("zabul","zabul","hamun","hamun")

for word in flattened_tweets:
    if word in wrong_spell:
    flattened_tweets[flattened_tweets.index(word)] = correct_spell[wrong_spell.index(word)]

fdist = FreqDist(flattened_tweets)
print(fdist.most_common(5))
fdist.plot(5, cumulative=False)
#endregion