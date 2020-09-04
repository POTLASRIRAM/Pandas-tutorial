#!/usr/bin/env python
# coding: utf-8

# ### Python is an open source library which provide's high performance and easy to use.Pandas is used as data analysis tool's for python.It is developed in 2008 by McKinney.

# ### 1. Installation and Loading Data

# #### Installation :
#       1.using pip
#       2.Anaconda

# #### Importing pandas

# In[1]:


import pandas as pd


# #### Loading dataset

# In[3]:


df = pd.read_csv("G:\downloads\survey\survey_results_public.csv")


# In[4]:


df


# In[11]:


df.info()


# In[12]:


df.shape


# In[6]:


df.tail(10)


# ### 2. Data frames and Series

# #### Data frames : A two-dimensional data structure(i.e rows and columns).

# ##### Creating data frame

# In[13]:


person={"name":["Sriram","Santhosh"],"age":[20,21],"email":["sriram@gmail.com","santhosh@gmail.com"]}


# In[14]:


p=pd.DataFrame(person)


# In[15]:


p


# #### Series : One dimensional data structure

# In[18]:


import numpy as np


# In[20]:


a=np.array([1,2,3,4,5,6,7])
pn=pd.Series(a)
pn


# ### 3. Index

# In[23]:


df


# #### Setting index

# In[24]:


df.set_index('Respondent',inplace=True)


# In[25]:


df


# In[26]:


df.index


# #### Resetting index

# In[27]:


df.reset_index(inplace=True)


# In[28]:


df


# #### Explicitly adding column names at the time of reading files

# In[34]:


sample=pd.read_csv("G:\downloads\sample.csv")


# In[35]:


sample


# In[36]:


a=["name","age","place"]


# In[44]:


sample=pd.read_csv("G:\downloads\sample.csv", names=(a))


# In[45]:


sample


# In[ ]:




