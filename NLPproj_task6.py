#region Description: task6
print('input is: tweets_words') #we need to have a sentences (not a list)
###################################################################################################
import sentistrength
from sentistrength import PySentiStr

senti= PySentiStr()
senti.setSentiStrengthPath('C:/Users/makbari19/Documents/SentiStrength.jar')
senti.setSentiStrengthLanguageFolderPath('C:/Users/makbari19/Documents/SentiStrengthData/')
senti.getSentiment(tweets_words)
