#region Description: task4
print('input is: flattened_tweets')
###########################################################################################
import tweepy

import nltk
#nltk.download() #use it and dl all-nltk

from nltk.tokenize import TweetTokenizer
from nltk.tokenize import MWETokenizer
from nltk.probability import FreqDist
from nltk.corpus import stopwords

POS_tweets=nltk.pos_tag(flattened_tweets)

name_tags=[tag for (word, tag) in POS_tweets if word=='kamal_khan']
print(name_tags)

#this is big picture of POS in our querry:
nltk.FreqDist(tag for (word, tag) in POS_tweets)

nltk.pos_tag('go'.split())
nltk.pos_tag('went'.split())
nltk.pos_tag('gone'.split())
nltk.pos_tag('going'.split())

#kamal_khan was wrongly tagged as verb! so we revise it here:
flattened_tweets_noun=[word for (word,tag) in POS_tweets if tag=='NN' or word=='kamal_khan']
flattened_tweets_verb=[word for (word,tag) in POS_tweets if tag=='VB' or tag=='VBD' or tag=='VBN' or tag=='VBG']

#here we revise wrong tags:
flattened_tweets_verb=[verb for verb in flattened_tweets_verb if verb != '😢' and verb != 'kamal_khan']

fdist_noun = FreqDist(flattened_tweets_noun)
most20_noun=fdist_noun.most_common(20)
print(most20_noun)
fdist_noun.plot(20, cumulative=False)

fdist_verb = FreqDist(flattened_tweets_verb)
most20_verb=fdist_verb.most_common(20)
print(most20_verb)
fdist_verb.plot(20, cumulative=False)
#endregion