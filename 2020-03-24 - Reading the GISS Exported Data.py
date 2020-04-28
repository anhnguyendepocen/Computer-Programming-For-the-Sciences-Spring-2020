#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


#     2020-03-24 - Reading the GISS Exported Data.ipynb

# In[2]:


from sci378 import *


# In[3]:


data=pd.read_csv("data/station_temperature_data.csv.gz",index_col=False)


# In[4]:


info=pd.read_excel("data/station_info.xlsx")


# In[5]:


info.head()


# In[6]:


info['Brightness']


# In[7]:


data.tail()


# In[8]:


station='BERKELEY'
x=data['time']
y=data[station]
plot(x,y,'-o')
title(station)


# In[9]:


x,y   # lots of nans!


# In[10]:


def get_xy(data,station):
    x,y=array(data[['time',station]].dropna()).T    
    return x,y


# In[11]:


x,y=get_xy(data,station)


# In[12]:


model=ols('y ~ x', data={'y':y,'x':x})
results=model.fit()
results.summary()


# In[13]:


xx=linspace(min(x)-10,max(x)+10,20)
yy=results.predict({'x':xx})

m=results.params['x']
mσ=results.bse['x']

b=results.params['Intercept']

plot(x,y,'-o')
title(station+" : y=%.3g (+/- %.4g) x + %.3g" % (m,mσ,b))
plot(xx,yy,'b-')


# In[14]:


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

# In[15]:


station_names=data.columns[2:]
station_names[:20]


# In[16]:


station='SHARJAH_INTER_AIRP'
info[info['Station']==station]


# In[17]:


float(info[info['Station']==station]['Brightness'])


# In[26]:


station='SAVE'


# In[28]:


a=array(info[info['Station']==station]['Brightness'])[0]


# In[31]:


type(a)


# In[37]:


S=Storage()
station_subset=[]
for station in station_names[:200]:
    #brightness=float(info[info['Station']==station]['Brightness'])
    brightness=array(info[info['Station']==station]['Brightness'])[0]
    latitude=array(info[info['Station']==station]['Latitude'])[0]
    longitude=array(info[info['Station']==station]['Longitude'])[0]
    elevation=array(info[info['Station']==station]['Elevation'])[0]
    x,y=get_xy(data,station)
    
    if len(x)==0:
        continue 
        
    model=ols('y ~ x', data={'y':y,'x':x})
    results=model.fit()
    m=results.params['x']
    mσ=results.bse['x']
    
    S+=brightness,m,mσ,latitude,longitude,elevation
    
    station_subset.append(station)
    print(station)
    
brightness,m,mσ,latitude,longitude,elevation= array(S)


# In[38]:


latitude


# In[39]:


m,mσ


# In[40]:


x=brightness
y=m
yerr=mσ


# In[41]:


plot(x,y,'o')


# In[42]:


errorbar(x,y,yerr,fmt='o');


# In[43]:


new_info=pd.DataFrame({
    'Station':station_subset,
    'm':m,
    'brightness':brightness,
    'longitude':longitude,
    'latitude':latitude,
    'elevation':elevation
})
new_info.to_excel('data/new_info.xlsx')
new_info


# In[29]:


len(elevation)


# In[53]:


info[info['Brightness']>150]


# In[ ]:




