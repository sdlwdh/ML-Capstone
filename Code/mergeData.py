#!/usr/bin/env python
# coding: utf-8

# In[39]:


import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[47]:


#list of csv names not to append
l=['Imputed with KNN=5.csv','CMU Data.csv','Merged Data.csv']

#Starting point for data alignment
#M=pd.read_csv('CMU Data.csv')
M=pd.read_csv('Imputed with KNN=5.csv',index_col=0)
M['Timestamp']=pd.to_datetime(M['Timestamp'])
M=M.set_index('Timestamp')

#read through each file 
for filename in os.listdir(os.getcwd()):
    if filename[-4:]=='.csv' and filename not in l:
        with open(os.path.join(os.getcwd(), filename), 'r') as f: # open in readonly mode
            N=pd.read_csv(filename)
            N.iloc[:,0]=pd.to_datetime(N.iloc[:,0].values)
            M=M.join(N.set_index(N.columns[0]),how='outer')
            #print(M.head())
            f.close()

M=M.iloc[::-1,:]
M.index.names = ['Time']

#save the final merged data
M.to_csv('Merged Data.csv')

