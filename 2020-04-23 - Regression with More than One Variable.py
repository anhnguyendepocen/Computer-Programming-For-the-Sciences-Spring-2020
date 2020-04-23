#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


from sci378 import *


# In[3]:


data=pd.read_excel('data/new_info.xlsx')
data


# In[5]:


model=ols('m ~ brightness',data=data)
results=model.fit()
results.summary()


# In[7]:


results.params


# In[8]:


model=ols('m ~ brightness + longitude + latitude',data=data)
results=model.fit()
results.summary()


# In[ ]:




