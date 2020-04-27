#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


from sci378 import *


# In[3]:


data=pd.read_csv('data/temperature.txt',delim_whitespace=True)
data


# In[17]:


t=array(data['Year'])-1880
T=array(data['Annual_Mean'])
plot(t,T,'-o')


# ## Linear Regression

# In[18]:


model=ols("y ~ x",data={'x':t,'y':T})
results=model.fit()
results.summary()


# In[19]:


results.params


# In[20]:


results.params.keys()


# In[21]:


slope=results.params['x']
slope_uncertainty=results.bse['x']
slope,slope_uncertainty


# In[26]:


xx=linspace(0,140,100)
yy=results.predict({'x':xx})
plot(t,T,'-o')
plot(xx,yy)


# ## Quadratic

# In[27]:


model=ols("y ~ x + I(x*x)",data={'x':t,'y':T})
results=model.fit()
results.summary()


# In[28]:


results.params


# In[29]:


results.params.keys()


# In[30]:


linear_parameter=results.params['x']
linear_parameter_uncertainty=results.bse['x']
linear_parameter,linear_parameter_uncertainty


# In[31]:


quadratic_parameter=results.params['I(x * x)']
quadratic_parameter_uncertainty=results.bse['I(x * x)']
quadratic_parameter,quadratic_parameter_uncertainty


# In[32]:


xx=linspace(0,140,100)
yy=results.predict({'x':xx})
plot(t,T,'-o')
plot(xx,yy)


# In[ ]:




