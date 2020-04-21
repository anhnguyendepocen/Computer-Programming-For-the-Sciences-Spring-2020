#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


from sci378 import *


# In[5]:


t=linspace(1900,2000,101)
T=10+(t-1900)*.5 + 5*rand(len(t))


# In[6]:


plot(t,T,'-o')


# In[9]:


polyfit(t-1950,T,1)


# In[10]:


polyfit(t,T,1)


# In[ ]:




