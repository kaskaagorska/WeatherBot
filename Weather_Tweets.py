#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Dependencies

import tweepy
import time
import json
import random
import requests as req
import datetime
from config import consumer_key, consumer_secret, access_token, access_token_secret, weather_api_key


# In[ ]:


# Twitter API Keys
consumer_key = consumer_key
consumer_secret = consumer_secret
access_token = access_token
access_token_secret = access_token_secret


# In[ ]:


# Save config information
url = "http://api.openweathermap.org/data/2.5/weather?"
city = "Washington, D.C."

# Build query URL
query_url = url + "appid=" + api_key + "&q=" + city



# In[ ]:


# Create a function that gets the weather in Washington, DC and Tweets it
def WeatherTweet():

    # Construct a Query URL for the OpenWeatherMap
    url = "http://api.openweathermap.org/data/2.5/weather?"
    city = "Washington, D.C."
    units = "imperial"
    query_url = url + "appid=" + api_key + "&q=" + city + "&units=" + units

    # Perform the API call to get the weather
    
    url = "http://api.openweathermap.org/data/2.5/weather?"
    city = "Washington, D.C."

    # Build query URL
    query_url = url + "appid=" + api_key + "&q=" + city

    # Twitter credentials

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())
    
    # Tweet the weather
    
 

    # Print success message


# In[ ]:


# Set timer to run every 1 hour


# In[ ]:




