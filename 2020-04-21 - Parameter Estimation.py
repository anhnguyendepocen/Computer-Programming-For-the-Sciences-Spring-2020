#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


from sci378 import *


# In[3]:


from pyndamics import Simulation
from pyndamics.emcee import *


# In[6]:


data=pd.read_csv('data/FluNetInteractiveReport.csv',skiprows=3)
data.head()


# In[17]:


t=array(data['Year']+(data['Week']-1)/52)
y=array(data['ALL_INF'])

y=y[(t>=2017.5) & (t<=2018.5)]
t=t[(t>=2017.5) & (t<=2018.5)]

t=(t-t[0])*365.25


# In[18]:


plot(t,y,'-o')


# In[19]:


sim=Simulation()
sim.add("N=S+I+R")
sim.add(" S' = -β*S*I/N",3e8)
sim.add(" I' = +β*S*I/N - γ*I",1,plot=True)
sim.add(" R' = +γ*I",0)
sim.add_data(t=t,I=y,plot=True)
sim.params(β=0.3,γ=0.1)
sim.run(0,365)


# In[27]:


sim=Simulation()
sim.add("N=S+I+R")
sim.add(" S' = -β*S*I/N",3e8)
sim.add(" I' = +β*S*I/N - γ*I",1,plot=True)
sim.add(" R' = +γ*I",0)
sim.add_data(t=t,I=y,plot=True)
sim.params(β=0.08,γ=0.06)
sim.run(0,365)


# In[29]:


t1=t[t<200]
y1=log(y[t<200])
plot(t1,y1,'-o')


# In[30]:


t1=t[(t<200) & (t>50)]
y1=log(y[(t<200) & (t>50)])
plot(t1,y1,'-o')


# In[31]:


model=ols('y ~ x', data={'y':y1,'x':t1})
results=model.fit()
results.summary()


# In[32]:


m=results.params['x']
m


# In[33]:


t2=t[(t>200) & (t<365)]
y2=log(y[(t>200) & (t<365)])
plot(t2,y2,'-o')


# In[35]:


model=ols('y ~ x', data={'y':y2,'x':t2})
results=model.fit()
print(results.summary())
m=results.params['x']
m


# In[45]:


sim=Simulation()
sim.add("N=S+I+R")
sim.add(" S' = -β*S*I/N",3e8)
sim.add(" I' = +β*S*I/N - γ*I",300,plot=True)
sim.add(" R' = +γ*I",0)
sim.add_data(t=t,I=y,plot=True)
sim.params(β=0.037,γ=0.03)
sim.run(0,365)


# In[62]:


model=MCMCModel(sim,
               β=Normal(0.05,2,all_positive=True),
               γ=Normal(0.05,2,all_positive=True),
               initial_I=Uniform(1,100),)


# In[63]:


model.run_mcmc(500,repeat=5)
model.plot_chains()


# In[64]:


sim.run(0,365)


# In[76]:


Ro=model.eval('β/γ')


# In[77]:


model.plot_distributions(Ro)


# In[78]:


model.plot_distributions()


# ## Measles in a school

# In[79]:


data=pd.read_excel('data/measles_hagelloch_1861.xlsx')
data.head()


# In[80]:


days=array(data['day'])
t=sorted(list(set(days)))
I=[]
for _ in t:
    I.append(sum(days==_))
t=array(t)
I=array(I)

t=t[:-1]
I=I[:-1]


# In[81]:


plot(t,I,'-o')


# In[82]:


t,I


# In[86]:


sim=Simulation()
sim.add("N=S+I+R")
sim.add("S'=-β*S*I/N",188)
sim.add("I'=β*S*I/N-γ*I",.1,plot=True)
sim.add("R'=γ*I",0)
sim.params(β=4,γ=4)
sim.add_data(t=t,I=I,plot=True)
sim.run(0,t.max())


# In[87]:


model=MCMCModel(sim,
                β=Normal(.4,.4),
                initial_I=Uniform(0,10),
                γ=Normal(.4,.4),
                )


# In[88]:


model.run_mcmc(500,repeat=2)
model.plot_chains()


# In[89]:


model.plot_distributions()


# In[95]:


model.plot_distributions(Ro=model.eval('β/γ'))


# In[91]:


sim.run(0,t.max())


# In[ ]:




