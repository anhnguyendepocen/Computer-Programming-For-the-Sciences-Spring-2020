#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from statsmodels.formula.api import ols


# ## Sklearn

# In[40]:


data = pd.read_csv('VIRAC.csv')
data=data.dropna()   #<==== have to drop the nans
x = data.iloc[:, 0].values.reshape(-1, 1)
y = data.iloc[:, 1].values.reshape(-1, 1)
linear_regressor = LinearRegression()
linear_regressor.fit(x, y)
y_pred = linear_regressor.predict(x)


# In[41]:


plt.plot(x, y,'-o')
plt.plot(x, y_pred, 'r')


# In[42]:


slope=linear_regressor.coef_
slope


# no uncertainties!

# ## Statsmodels OLS

# In[43]:


data = pd.read_csv('VIRAC.csv')
x = array(data['Year'])
y = array(data['Temperature'])
model=ols("y ~ x",data={'y':y,'x':x})
result=model.fit()
y_pred = result.predict({'x':x})


# In[44]:


plt.plot(x, y,'-o')
plt.plot(x, y_pred, 'r')


# In[45]:


result.summary()


# In[46]:


slope=result.params['x']
slope_uncertainty=result.bse['x']
print("Slope = %.3g +- %.3g" % (slope,slope_uncertainty))


# In[47]:


x,y


# In[ ]:




