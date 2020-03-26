#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# a. you draw with replacement and observe the following sequence:  2,5,9,3,6,4
# 
# b. you draw without replacement and observe the following sequence:  2,5,9,3,6,4

# In[4]:


P_H = (2/55 * 5/55) * 1/2  # numerator of Bayes  with replacement
P_L = (9/55 * 4/55) * 1/2


# In[5]:


P_H,P_L


# In[6]:


K=P_H+P_L


# In[7]:


P_H=P_H/K
P_L=P_L/K


# In[8]:


P_H,P_L


# In[9]:


P_H = (2/55 * 5/54) * 1/2  # numerator of Bayes  without replacement
P_L = (9/55 * 4/54) * 1/2


# In[ ]:




