#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install requests


# In[2]:


pip install beautifulsoup4


# In[3]:


import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd


# In[4]:


url="https://www.naukri.com/financial-analyst-jobs-in-mumbai?k=financial%20analyst&l=mumbai"


# In[5]:


page = requests.get(url)


# In[6]:


page.text


# In[7]:


driver = webdriver.Chrome()
driver.get("https://www.naukri.com/financial-analyst-jobs-in-mumbai?k=financial%20analyst&l=mumbai")



print (driver.title)
print (driver.current_url)

soup = BeautifulSoup(driver.page_source,'html5lib')
print(soup.prettify())

driver.close()


# In[8]:


df = pd.DataFrame(columns=['Title','Company','Ratings','Reviews'])


# In[9]:


results= soup.find(class_='list')


# In[10]:


results


# In[11]:


job_elems = results.find_all('article',class_='jobTuple bgWhite br4 mb-8')


# In[12]:





for job_elem in job_elems:
    URL = job_elem.find('a',class_='title fw500 ellipsis').get('href')
    print(URL)
   
   
    Title = job_elem.find('a',class_='title fw500 ellipsis')
    print(Title.text)
   
   
   
   
    rating_span = job_elem.find('span',class_='starRating fleft dot')
    if rating_span is None:
        continue
    else:
        Ratings = rating_span.text
    print(Ratings)
   
    Review_span = job_elem.find('a',class_='reviewsCount ml-5 fleft blue-text')
    if Review_span is None:
        continue
    else:
        Reviews = Review_span.text
    print(Reviews)
   
   
   
    print(" "*2)


# In[13]:


for job_elem in job_elems:
    URL = job_elem.find('a',class_='title fw500 ellipsis').get('href')
    print(URL)
   
    Title = job_elem.find('a',class_='title fw500 ellipsis')
    print()
   
    Company = job_elem.find('a',class_='subTitle ellipsis fleft')
    print()
   
   
    rating_span = job_elem.find('span',class_='starRating fleft dot')
    if rating_span is None:
        continue
    else:
        Ratings = rating_span.text
    print(Ratings)
   
   
   
    Review_span = job_elem.find('a',class_='reviewsCount ml-5 fleft blue-text')
    if Review_span is None:
        continue
    else:
        Reviews = Review_span.text
    print(Reviews)
   
    print(" "*2)
    
    df=df.append({'URL':URL,'Title':Title.text,'Company': Company.text,'Ratings':Ratings,'Reviews':Reviews},ignore_index = True)


# In[14]:


df.to_csv("Naukri.com_Data.csv",index=False)


# In[15]:


df.columns


# In[16]:


df.head()


# In[ ]:





# In[17]:


import csv


# In[18]:


data= pd.read_csv("Naukri.com_Data.csv")
data


# In[20]:


df.dtypes


# In[21]:


import seaborn as sns


# In[22]:


sns.countplot(data['Ratings'])


# In[23]:


sns.countplot(data['Reviews'])


# In[24]:


sns.countplot(data['Title'])


# In[27]:


sns.countplot(data['Company'])


# In[ ]:




