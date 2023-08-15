import tweepy
import requests
from bs4 import BeautifulSoup
import re
import time
import random
import credentials


# we chose "tomorrow" instead of "today" because wikipedia for some reason has one day delay ¿?
url = 'https://en.wikipedia.org/wiki/Wikipedia:On_this_day/Tomorrow'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')


articles = soup.find_all('li')
article_l = [] #generate an empty list that will store the future values found in the website
for i in range(0,len(articles)):
    global article #article is a global variable
    article = soup.find_all('li')
    article = articles[i].text
    s = re.compile("\d\d\d\d.*") # regex search to match any text starting by 4 digits (wikipedia starts from the year and then the fact)
    article = s.match(article)# the regex compiled above starts searching
    if article: # in case of a match it returns the value
        article = article.group(0) #returns the value
        article_l.append(article) # appends the value to our list "article_l"


# Now the part where we send the tweet

consumer_key = credentials.consumer_key
consumer_secret = credentials.consumer_secret
access_token = credentials.access_token
access_token_secret = credentials.access_token_secret

# authentication
client = tweepy.Client(
                    bearer_token=credentials.bearer_token,
                    consumer_key=credentials.consumer_key,
                    consumer_secret=credentials.consumer_secret,
                    access_token=credentials.access_token,
                    access_token_secret=credentials.access_token_secret
                    )

time.sleep(random.randrange(0,1800)) #the first tweet will got at a random time within the first 30 minutes once it executes

# now the tweets
for i in range(len(article_l)):
    client.create_tweet(text = "#OnThisDayInHistory: " + re.sub(r'\(.*?\)', '', article_l[i]))
    #random time between tweets
    time.sleep(random.randrange(9000,12600))