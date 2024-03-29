#region Description: task1
#1. In this code we retrieve a querry from twitter:

#please define below:

#D+
name = 'D+'
keyword1= '(Hamun Lake blue)'
keyword2= '(زیبایی سیستان)'
keyword3= '(زیبایی زابل)'
keyword4= '(توریست سیستان)'
keyword5= '(دریاچه هامون زیبا)'
keyword6= '(چاه نیمه ها)'
keyword7= '(هامون پر آب)'
keyword8= '(Hamun Lake beautiful)'
'''
#D-
name = 'D-'
keyword1= '(دریاچه هامون)'
keyword2= '(گرد و عبار زابل)'
keyword3= '(بیکاری سیستان)'
keyword4= '(خشکسالی سیستان)'
keyword5= '(تشنگی سیستان)'
keyword6= '(تشنگی زابل)'
keyword7= '(تشنگی دریاچه هامون)'
keyword8= '(Hamun Lake)'
'''
#########################################

query=keyword1+' OR '+keyword2+' OR '+keyword3+' OR ' +keyword4+' OR ' +keyword5 +' OR ' +keyword6+' OR ' +keyword7+' OR ' +keyword8+' -is:retweet'

import tweepy

import pandas as pd

import googletrans

from googletrans import Translator
translator = Translator()

from datetime import datetime

import time

import re

def limit_handled(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            time.sleep(15 * 60)
        except StopIteration:
            print('Query is done :)')
            break

consumer_key='ebbdxA3pLDjiYKRgkmEQAht4L'
consumer_secret='P1fDSQedNPrDn5nNeuxde6AndwrUTt7Rfwdu4ojKRs82opU48K'
token_access='1145059218212425728-pY9jVhgbZNlSaNtFsMGmXZUDi5I3Rv'
token_secret='Awb9UVFUX5yMuDYIE7h6mX2RIDmgmPV7O3YA3xuWB8Ng7'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)

auth.set_access_token(token_access,token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

me=api.me() #here you get your own account address

print(me.screen_name)

#Search tweets

tweets_data=[]

for i,status in enumerate(limit_handled(tweepy.Cursor(api.search, q=query).items())):
    status_dict=dict(vars(status))
    tweet=status_dict['text']
    print(i, tweet)
    tweets_data.append(tweet)

df = pd.DataFrame(tweets_data)

#query_en=translator.translate(keyword, dest='en').text
#name= query_en + '_raw_' + str(len(tweets_data)) + '.csv'

df.to_csv(name + '.csv', sep='\t', header=False, encoding='utf-8-sig')
#endregion
