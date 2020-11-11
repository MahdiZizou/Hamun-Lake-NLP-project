#region Description: task2
print('you should execute line by line because run does not work on seperate py files')
print('input is: tweets_data')
print('Your querry was:', query)
print('The length of tweet data  set is:', len(tweets_data))
####################################################################################################
import tweepy
import pandas as pd
import googletrans
from googletrans import Translator
translator = Translator()

# here we clean and translate tweets:
translated_tweet = []
for tweet in tweets_data:
    clean_tweet = "".join(
        [char for char in tweet if
         char not in 'qwertyuiopasdfghjkl\:zxcvbnm/ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890@#$%^&*_=-_,:.;?!']
    ).strip()

    clean_tweet_trans = translator.translate(clean_tweet, src='fa', dest='en').text

    clean_tweet_trans_clean = "".join(
        [char for char in clean_tweet_trans if char not in ',:;،ضصثقفغعهخحجچپگکمنتالبیسشظطزرذدئوې']
    ).strip()

    # print(clean_tweet_trans_clean)
    translated_tweet.append(clean_tweet_trans_clean)

# here we change into pandas dataframe to save as csv:
df = pd.DataFrame(translated_tweet)
df.head()
query_en=translator.translate(keyword, dest='en').text
name= query_en + '_tranCln_' + str(len(tweets_data)) + '.csv'
df.to_csv(name, sep='\t', header=False, encoding='utf-8-sig')
print('DF is saved :)')
#endregion