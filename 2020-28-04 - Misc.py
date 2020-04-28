#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


from sci378 import *


# In[10]:


ls data


# In[11]:


ls data/crichton


# In[12]:


from glob import glob


# In[13]:


glob('data/*.xls')


# In[14]:


glob('data/*.csv')


# In[15]:


glob('data/*.xlsx')


# In[17]:


glob('data/*.xls*')


# In[21]:


fnames=glob('data/*.xlsx')


# In[23]:


for filename in fnames:
    print(filename)
    data=pd.read_excel(filename)
    display(data.head())


# In[24]:


data=pd.read_csv('data/temperature.txt',delim_whitespace=True)
data


# In[28]:


data['Annual_Mean']=data['Annual_Mean']/10


# In[29]:


data


# In[ ]:




