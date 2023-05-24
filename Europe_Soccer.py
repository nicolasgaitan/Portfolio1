#!/usr/bin/env python
# coding: utf-8

# #### Import libraries that are going to be used

# In[29]:


import requests
import pandas as pd
from bs4 import BeautifulSoup


# <br>

# #### The websites we are going to be scraping are below. We will be scraping all the soccer players from the top 5 European leagues and the standings for all European teams.
# 

# In[30]:


players_url = 'https://fbref.com/en/comps/Big5/stats/players/Big-5-European-Leagues-Stats'
standings_url = 'https://fbref.com/en/comps/Big5/Big-5-European-Leagues-Stats'


# <br>

# #### Scraping the players data

# In[31]:


p_data = requests.get(players_url)


# In[32]:


soup = BeautifulSoup(p_data.text)


# In[33]:


tables = soup.find_all('table')[0]


# In[34]:


players = pd.read_html(p_data.text, match = 'Player Standard Stats')[0]
players.columns = players.columns.droplevel()
players


# <br>

# #### Scraping the standings data

# In[35]:


s_data = requests.get(standings_url)


# In[36]:


soup = BeautifulSoup(s_data.text)


# In[40]:


standings = pd.read_html(s_data.text , match  = 'Big 5 Table')[0]


# In[41]:


standings


# <br>

# #### Converting the Players and Standings df into a csv. This file will will saved in our data folder and will be used for SQL/Tableau

# In[42]:


standings.to_csv('/users/nicolasgaitan/desktop/data/standings.csv', index=False)
players.to_csv('/users/nicolasgaitan/desktop/data/players.csv', index=False)

