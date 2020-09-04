# ### Pandas Day-2

# In[139]:


import numpy as np
import pandas as pd


# In[140]:


data={"name":["Sriram","Santhosh","john","danny","surya","singham"],"place":["america","australia","bangladesh","singapore","Tamil Nadu","Rajole"],"email":["sriram@gmail.com","santhosh@gmail.com","john@gmail.com","danny@gmail.com","surya@gmail.com","singham@gmail.com"]}


# In[141]:


df=pd.DataFrame(data)


# In[142]:


df


# ### Filters

# In[143]:


filt=(df['name']=="john")
df[filt]


# In[144]:


filt=(df['name']=="singham")
df[filt].place


# ### Updating Row's and Column's

# In[126]:


#Renaming column name's
df


# In[127]:


df.columns


# In[145]:


df.columns=['Person_name','Native_place','email']


# In[146]:


df


# In[130]:


# Changing the column names to upper case
df.columns=[x.upper() for x in df.columns]


# In[131]:


df


# In[132]:


# Replacing underscore's
df.columns=df.columns.str.replace('_',' ')


# In[133]:


df


# In[147]:


# Changing to lower case
df.columns=[x.lower() for x in df.columns]


# In[148]:


df


# In[149]:


# Renaming back to original names
df.rename(columns={'person_name':'Name','native_place':'place','email':'e_mail'},inplace=True)


# In[150]:


df


# #### loc and iloc

# In[42]:


# loc
df.loc[2:4,['place']]="sydney"


# In[43]:


df


# In[46]:


# iloc
df.iloc[2:3,2]


# In[47]:


df.iloc[2,2]="johnny@gmail.com"


# In[48]:


df


# ### Add or Removing columns and rows

# In[64]:


d={"first":["sriram","john"],"last":["potla","boltman"]}


# In[65]:


dd=pd.DataFrame(d)


# In[66]:


dd


# In[67]:


dd['Full name']=dd['first']+''+dd['last']


# In[68]:


dd


# In[69]:


# Removing columns
dd.drop(columns=['first','last'],inplace=True)


# In[70]:


dd


# In[82]:


df


# In[87]:


# Adding rows
df.append({'Name':'Vaag','place':'wgl','e_mail':'vaag@mail.com'},ignore_index=True)


# In[96]:


df.drop(df.index[[5]],inplace=True)


# In[97]:


df


# In[98]:


df


# In[105]:


# Adding new row
new_row={"Name":"King","place":"london","e_mail":"king@gmail.com"}


# In[106]:


df = df.append(new_row, ignore_index=True)


# In[107]:


df


# In[111]:


# Remove rows
# 1
df.drop(index=5,inplace=True)


# In[112]:


df


# In[151]:


# 2
# deleting row by using some value
df.drop(index=df[df['e_mail']=='sriram@gmail.com'].index)


# In[114]:


df


# In[115]:


filt=(df['place']=='america')
df.drop(index=df[filt].index)


# In[117]:


df


# In[ ]:




