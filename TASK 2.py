#!/usr/bin/env python
# coding: utf-8

# In[4]:


import nltk


# In[5]:


#1.frequency distribution function word in text
text='Up to the 1980s, most natural language processing systems were based on complex sets of hand-written rules. Starting in the late 1980s, however, there was a revolution in natural language processing with the introduction of machine learning algorithms for language processing.'
fd=nltk.FreqDist(text.split())
fd


# In[6]:


#2.conditional distribution 
from nltk.probability import ConditionalFreqDist


# In[7]:


cfd=ConditionalFreqDist((len(word),word) for word in text.split())


# In[8]:


cfd[4]


# In[10]:


#chinese segmentation using jieba
get_ipython().system('pip install jieba')


# In[14]:


pip install --upgrade pip


# In[15]:


#chinese segmentation using jieba
get_ipython().system('pip install jieba')


# In[16]:


import jieba


# In[17]:


seg=jieba.cut("網站有中、英文版本，也有繁、簡體版，可通過每頁左上角的連結隨時調整",cut_all=True)


# In[18]:


seg


# In[19]:


print(" ".join(seg))


# In[25]:


#4
import nltk
sent="Become an Expert in NLP"
words=nltk.word_tokenize(sent)
print(words)


# In[29]:


import nltk


# In[35]:


#5
texts="APJ Abdul Kalam was unique man. The most remarkable aspect of this man was his leaping optimism, positive attitude even amidst frustrating circumstances. While addressing the ISRO scientists in Trivandrum he showed remarkable positivity in science, politics and journalism and everything he touched upon and looked forward to India planting the tricolor on the moon when PSLV faced some failures! At the INS meeting at Kalpakkam in 2003, he overruled Chairman AEC and suggested a much higher target for the projected nuclear power in India. His impatience to find applications of his research in other fields resulted in the development of a metallurgical alloy for designing artificial limbs which was 1/10th weight of the normal ones and using his innovation to design a cheaper coronary stent."
for text in texts:
    sentences=nltk.sent_tokenize(text)
    for sentence in sentences:
        word=nltk.word_tokenize(sentence)
        print(word)
        tagged=nltk.pos_tag(words)
        print(tagged)
        


# In[ ]:




