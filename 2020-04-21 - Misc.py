#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


from sci378 import *


# In[3]:


t=linspace(1900,2000,101)
T=10+(t-1900)*.5 + 5*rand(len(t))


# In[4]:


plot(t,T,'-o')


# In[5]:


polyfit(t-1950,T,1)


# In[6]:


polyfit(t,T,1)


# In[7]:


from pyndamics import *


# In[8]:


t=linspace(0,10,100)
S=sin(t*3)
plot(t,S)


# In[9]:


t=linspace(0,10,100)  # made up data, you can use the real thing
values=sin(t*3)


# In[10]:


sim=Simulation()
sim.add("v'=F(t)/m",0,plot=True)
sim.add("x'=v",0,plot=True)
sim.params(m=1)
sim.add_interp_function(t=t,F=values)
sim.run(0,10)


# In[ ]:




