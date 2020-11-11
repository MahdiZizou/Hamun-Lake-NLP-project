# Hamun-Lake-NLP-project
In this project we retrieve tweets about Hamun Lake dessication. We have two branches in our repository as main and master.
8 below taks are defined and each are solved by python codes with the same as below task numbers uploaded as .py files in master branch. Also, two othe files are uploaded as Project_outcome.ppt and Project_report.docx in manin branch to explain outcomes of the project:
1.	Select appropriate keywords based on your own knowledge of the topic to collect Twitter dataset related to Hamun Lake desiccation and Positive citizen feeling using Twitter API, possibly, selecting Iranian language to increase the chance of collecting large data sample (D1). Repeat this process to collect data associated to related to Hamun Lake desiccation and Negative citizen feeling (D2). You should few keywords that stand for positive / negative citizen feeling. You may create your own Twitter developer account to enable you to collect data or use some existing ones elsewhere. Make sure you collect enough –at least one thousand tweets per country to enable useful comparison. Store the two dataset D1 and D2 in the same database
2.	Use Open translation API to translate all non-English tweets to English, although this is not a mandatory step if you manage to use multilingual parser.
3.	Use TweetTokenizer package to tokenize the tweet messages and use use MWETokenizer in order to handle composed words. Draw histogram of the most common terms, excluding stop-words, for D1 and D2
4.	Draw histogram of the 20 most co-occurring words, excluding stopwords, where one of the word is a verb and the other one is a noun (should use par-of speech tagger to identify part of speech of individual word in the tweet message), for each of D1 and D2. Comment on the discussion topics for each country accordingly.
5.	Use wordCloud  (see an example at https://www.geeksforgeeks.org/generating-word-cloud-python/ ) to draw a graphical representation of the words present in D1 and D2
6.	Use SentiStrength to determine the global sentiment associated to D1 and D2.  Discuss the finding with respect to the nature of D1 and D2 which are meant to represent positive and negative sentiment, respectively.
7.	Consider categories generated by Empath Client https:// HYPERLINK "https://github.com/Ejhfast/empath-client"github.com/Ejhfast/empath-client. Apply Empath Client to D1 and D2 class,  and report those categories who held non-zero weights. Record these findings in database, where for each tweet message, assign the corresponding set of Empath categories.
8.	We want to replicate the reasoning of WebJaccard similarity –see paper “WebSim: A web based semantic similarity measure” in Proc. of the 21st Annual Conference of the Japanese Society of Artificial Intelligence, 2007. 