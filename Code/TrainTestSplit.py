#!/usr/bin/env python
# coding: utf-8

# In[15]:


import numpy as np
import pandas as pd

#train/test based on 80/20 ratio

#read raw merged data: daily
df=pd.read_csv('20201029_ScrubbedDaily_Returns.csv')
df['Time']=pd.to_datetime(df['Time'])#,format='%Y-%m-%d')

train_to='2018/08/28'

train=df[df['Time']<train_to]
test=df[df['Time']>=train_to]

train.to_csv('train_daily.csv')
test.to_csv('test_daily.csv')


# In[16]:


#read raw merged data: weekly
df=pd.read_csv('20201029_ScrubbedWeekly_Returns.csv')
df['Time']=pd.to_datetime(df['Time'])#,format='%Y-%m-%d')

train=df[df['Time']<train_to]
test=df[df['Time']>=train_to]

train.to_csv('train_weekly.csv')
test.to_csv('test_weekly.csv')


# In[ ]:




