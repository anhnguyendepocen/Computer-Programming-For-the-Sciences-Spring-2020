#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


from sci378 import *


# In[3]:


data=pd.read_csv("data/station_temperature_data.csv.gz",index_col=False)


# In[4]:


info=pd.read_excel("data/station_info.xlsx")


# In[5]:


info.head()


# In[6]:


data.tail()


# In[7]:


station='BERKELEY'
x=data['time']
y=data[station]
plot(x,y,'-o')
title(station)


# In[35]:


x,y   # lots of nans!


# In[26]:


def get_xy(data,station):
    x,y=array(data[['time',station]].dropna()).T    
    return x,y


# In[37]:


x,y=get_xy(data,station)


# In[38]:


model=ols('y ~ x', data={'y':y,'x':x})
results=model.fit()
results.summary()


# In[46]:


xx=linspace(min(x)-10,max(x)+10,20)
yy=results.predict({'x':xx})

m=results.params['x']
mσ=results.bse['x']

b=results.params['Intercept']

plot(x,y,'-o')
title(station+" : y=%.3g (+/- %.4g) x + %.3g" % (m,mσ,b))
plot(xx,yy,'b-')


# In[45]:


results.bse


# ## go through all the stations
# 
# **is there a relationship between the temperature trend and brightness?**
# 
# (ideally) 20,000 stations
# 
# 1. x variable: brightness - 20,000 values
# 2. y variable: slope - 20,000 values
# 
# ### Recipe
# 
# 1. loop through stations, for each:
#     1. get the brightness
#     2. get the trends (slope)
#     3. get the slope uncertainties (m-σ)
#     3. add them to lists/Storage
# 
# things to consider
# 
# 1. weighted by the m-σ
# 2. errorbars

# In[9]:


station_names=data.columns[2:]
station_names[:20]


# In[11]:


station='SHARJAH_INTER_AIRP'
info[info['Station']==station]


# In[14]:


float(info[info['Station']==station]['Brightness'])


# In[33]:


station='SAVE'


# In[38]:


array(info[info['Station']==station]['Brightness'])[0]


# In[ ]:





# In[47]:


S=Storage()
for station in station_names[:200]:
    #brightness=float(info[info['Station']==station]['Brightness'])
    brightness=array(info[info['Station']==station]['Brightness'])[0]
    x,y=get_xy(data,station)
    
    if len(x)==0:
        continue 
        
    model=ols('y ~ x', data={'y':y,'x':x})
    results=model.fit()
    m=results.params['x']
    mσ=results.bse['x']
    
    S+=brightness,m,mσ
    print(station)
    
brightness,m,mσ = array(S)


# In[48]:


brightness


# In[49]:


m,mσ


# In[50]:


x=brightness
y=m
yerr=mσ


# In[51]:


plot(x,y,'o')


# In[52]:


errorbar(x,y,yerr,fmt='o');


# In[ ]:




