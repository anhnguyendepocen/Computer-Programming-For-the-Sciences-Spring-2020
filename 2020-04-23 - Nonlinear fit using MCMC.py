#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


from sci378 import *


# In[3]:


data=pd.read_csv('data/temperature.txt',delim_whitespace=True)
data


# In[4]:


t=array(data['Year'])
T=array(data['Annual_Mean'])
plot(t,T,'-o')


# In[6]:


from sie.mcmc import MCMCModel,Uniform,Normal,Jeffreys


# ## Fit to Linear, as an Example

# In[7]:


def P_data(data,m,b,σ):
    x,y=data
    μ=m*x+b     # y ~ μ + random
    distribution=Normal(μ,σ)
    return sum(distribution(y))


# In[10]:


data=t,T
model=MCMCModel(data,P_data,
                m=Normal(0,10),
                b=Uniform(-100,100),
                σ=Jeffreys(),
               )


# In[11]:


for i in range(2):
    model.run_mcmc(500)
model.plot_chains()


# In[12]:


model.plot_distributions()


# In[20]:


model.best_estimates()


# In[24]:


figure(figsize=(14,10))
plot(t,T,'-o')

m=model.best_estimates()['m'][1]
b=model.best_estimates()['b'][1]

μ=m*t+b
plot(t,μ,'-')


# In[23]:


m


# ## Fit to Non-Linear

# In[28]:


def P_data(data,a0,a1,a2,σ):
    x,y=data
    μ=a0+a1*x+a2*x*x
    distribution=Normal(μ,σ)
    return sum(distribution(y))


# In[33]:


data=t,T
model=MCMCModel(data,P_data,
                a0=Uniform(-1000,1000),
                a1=Normal(0,10),
                a2=Normal(0,10),
                σ=Jeffreys(),
               )


# In[34]:


for i in range(2):
    model.run_mcmc(500)
model.plot_chains()


# In[35]:


model.plot_distributions()


# In[36]:


figure(figsize=(14,10))
plot(t,T,'-o')

a0=model.best_estimates()['a0'][1]
a1=model.best_estimates()['a1'][1]
a2=model.best_estimates()['a2'][1]

μ=a0+a1*t+a2*t*t
plot(t,μ,'-')


# In[ ]:




