#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


from sci378 import *


# In[6]:


filename='data/crichton/berkeley.csv'
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


# In[7]:


filename='data/crichton/pasadena.csv'
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


# In[9]:


for filename in ['data/crichton/berkeley.csv','data/crichton/pasadena.csv']:
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


# In[10]:


from glob import glob

filenames=glob('data/crichton/*.csv')
filenames


# In[11]:


filenames=glob('data/crichton/b*.csv')
filenames


# In[12]:


filenames=glob('data/crichton/*.csv')

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


# In[16]:


filenames=glob('data/crichton/*.csv')

storage=Storage()

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

    
    storage+=m,mσ
#     figure()
#     plot(x,y,'-o')
#     ylabel('Temperature [C]')
#     title(filename+" : y=%.3g (+/- %.4g) x + %.3g" % (m,mσ,b))
#     plot(xx,yy,'b-')

m,mσ=array(storage)


# In[14]:


m


# In[15]:


mσ


# In[ ]:




