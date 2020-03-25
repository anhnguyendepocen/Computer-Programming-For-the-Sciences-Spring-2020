#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


from sci378 import *


# In[3]:


filename='data/berkeley.csv'
data=pd.read_csv(filename)

x=array(data['YEAR'])
y=array(data['metANN'])
y[y==999.9]=nan

model=ols('y ~ x', data={'y':y,'x':x})
results=model.fit()

xx=linspace(min(x)-10,max(x)+10,20)
yy=results.predict({'x':xx})

m=results.params['x']
mσ=results.bse['x']

b=results.params['Intercept']

plot(x,y,'-o')
ylabel('Temperature [C]')
title(filename+" : y=%.3g (+/- %.4g) x + %.3g" % (m,mσ,b))
plot(xx,yy,'b-')


# In[5]:


for filename in ['data/berkeley.csv','data/pasadena.csv']:
    data=pd.read_csv(filename)

    x=array(data['YEAR'])
    y=array(data['metANN'])
    y[y==999.9]=nan

    model=ols('y ~ x', data={'y':y,'x':x})
    results=model.fit()

    xx=linspace(min(x)-10,max(x)+10,20)
    yy=results.predict({'x':xx})

    m=results.params['x']
    mσ=results.bse['x']

    b=results.params['Intercept']

    figure()
    plot(x,y,'-o')
    ylabel('Temperature [C]')
    title(filename+" : y=%.3g (+/- %.4g) x + %.3g" % (m,mσ,b))
    plot(xx,yy,'b-')


# In[6]:


from glob import glob


# In[10]:


filenames=glob('data/*.csv')
filenames


# In[12]:


filenames=filenames[:2]
filenames


# In[14]:


for filename in filenames:
    data=pd.read_csv(filename)

    x=array(data['YEAR'])
    y=array(data['metANN'])
    y[y==999.9]=nan

    model=ols('y ~ x', data={'y':y,'x':x})
    results=model.fit()

    xx=linspace(min(x)-10,max(x)+10,20)
    yy=results.predict({'x':xx})

    m=results.params['x']
    mσ=results.bse['x']

    b=results.params['Intercept']

    figure()
    plot(x,y,'-o')
    ylabel('Temperature [C]')
    title(filename+" : y=%.3g (+/- %.4g) x + %.3g" % (m,mσ,b))
    plot(xx,yy,'b-')


# In[21]:


slopes={}
slope_sigmas={}
significant_trend={}

for filename in filenames:
    data=pd.read_csv(filename)

    x=array(data['YEAR'])
    y=array(data['metANN'])
    y[y==999.9]=nan

    model=ols('y ~ x', data={'y':y,'x':x})
    results=model.fit()

    xx=linspace(min(x)-10,max(x)+10,20)
    yy=results.predict({'x':xx})

    m=results.params['x']
    mσ=results.bse['x']

    b=results.params['Intercept']

    
    slopes[filename]=m
    slope_sigmas[filename]=mσ
    
    
    if m>0:
        if (m-2*mσ)>0:
            significant_trend[filename]=True
        else:
            significant_trend[filename]=False
            
            
            


# In[22]:


slopes


# In[23]:


slope_sigmas


# In[24]:


significant_trend


# ## linspace

# In[25]:


linspace(0,10,11)


# In[26]:


linspace(0,10,101)


# In[27]:


linspace(30,40,101)


# In[28]:


linspace(0,5,17)


# In[30]:


x=linspace(-10,10,500)
y=x**2*sin(x)
plot(x,y)

x=linspace(-10,10,20)
y=x**2*sin(x)
plot(x,y)


# In[31]:


x=linspace(0,1,500)
y=x**2*sin(x)
plot(x,y)


# In[32]:


x=linspace(0,1,500)
y=exp(-x**2)
plot(x,y)


# In[35]:


x=linspace(-10,10,500)
dx=x[1]-x[0]


y=exp(-x**2)
plot(x,y)


# normalized means
# 
# $$
# \int_{-\infty}^{+\infty} y(x) dx = 1
# $$

# In[38]:


sum(y*dx)


# In[39]:


y=y/sum(y*dx)  # this normalizes it


# In[40]:


sum(y*dx)


# In[ ]:





# In[41]:


sum(y[x>1]*dx)


# # do a half-normal

# In[42]:


x=linspace(-10,10,500)
dx=x[1]-x[0]

y=exp(-x**2)
y[x<0]=0
y=y/sum(y*dx)  # this normalizes it


plot(x,y)


# In[43]:


x=linspace(0,10,500)
dx=x[1]-x[0]

y=exp(-x**2)
y=y/sum(y*dx)  # this normalizes it


plot(x,y)


# In[ ]:




