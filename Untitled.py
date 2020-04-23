#!/usr/bin/env python
# coding: utf-8

# In[2]:


import xport.v56

with open('/Users/bblais/Downloads/CARB_E.XPT', 'rb') as f:
    library = xport.v56.load(f)


# In[4]:


library.sas_version


# In[5]:


import pandas


# In[6]:


pandas.__version__


# In[7]:


get_ipython().run_line_magic('pylab', 'inline')


# In[8]:


a=array([1,2,3,4])


# In[9]:


a


# In[11]:


a.dtype


# In[12]:


a[2]=2.3


# In[13]:


a


# In[14]:


a.dtype


# In[15]:


a.dtype=float


# In[16]:


a


# In[17]:


a=array([1,2,3,4])


# In[18]:


a=array(a,float)


# In[19]:


a


# In[20]:


a[2]=2.3


# In[21]:


a


# In[22]:


a.astype(int)


# In[23]:


a


# In[ ]:




