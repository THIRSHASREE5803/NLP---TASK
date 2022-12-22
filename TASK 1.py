#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk


# In[2]:


from nltk.book import *


# In[3]:


nltk.download()


# In[4]:


from nltk.corpus import brown


# In[5]:


brown.categories()


# In[6]:


brown.words(categories='news')[:10]


# In[7]:


brown.words(categories='news')[:]


# In[8]:


from nltk.corpus import inaugural


# In[10]:


inaugural.fileids()


# In[11]:


inaugural.words(fileids='1861-Lincoln.txt')[:10]


# In[12]:


inaugural.words(fileids='2009-Obama.txt')[:10]


# In[14]:


inaugural.words(fileids='2017-Trump.txt')[:30]


# In[ ]:




