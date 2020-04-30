#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[3]:


from sci378 import *


# In[4]:


x=linspace(-10,10,100)

for i in range(5):
    
    b=0
    m=randn()
    y=m*x+b + rand(len(x))
    
    plot(x,y)


# In[5]:


x=linspace(-10,10,100)

for i in range(5):
    
    b=0
    m=randn()
    y=m*x+b + rand(len(x))
    
    plot(x,y,'b-')


# In[6]:


x=linspace(-10,10,100)

for i in range(5):
    
    b=0
    m=randn()
    y=m*x+b + rand(len(x))
    
    figure()
    plot(x,y,'b-')


# In[ ]:




