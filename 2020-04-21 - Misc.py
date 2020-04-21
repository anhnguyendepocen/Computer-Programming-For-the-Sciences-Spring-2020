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


# In[3]:


from pyndamics import *


# In[5]:


t=linspace(0,10,100)
S=sin(t*3)
plot(t,S)


# In[17]:


class InterpData(object):
    
    def __init__(self,x,y,name):
        self.x=x
        self.y=y
        self.__name__=name
        
    def __call__(self,x):
        from numpy import interp
        y=interp(x,self.x,self.y)
        return y

t=linspace(0,10,100)  # made up data, you can use the real thing
S=sin(t*3)

F=InterpData(t,S,'F')


# In[18]:


sim=Simulation()
sim.add("v'=F(t)/m",0,plot=True)
sim.add("x'=v",0,plot=True)
sim.params(m=1)
sim.functions(F)
sim.run(0,10)


# In[10]:


dir(sim)


# In[11]:


get_ipython().run_line_magic('pinfo', 'sim.functions')


# In[ ]:




