#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
data = {
    "Location1": [100, 50, 300, 200, 80],
    "Location2": [200, 60, 400, 250, 90],
    "Location3": [150, 40, 350, 220, 70],
    "Location4": [300, 80, 500, 270, 100]
}
inventory = pd.DataFrame(data, index=["Product1", "Product2", "Product3", "Product4", "Product5"])


# In[3]:


print(inventory.head(2))


# In[4]:


print(inventory.shape)


# In[5]:


print(inventory.columns.tolist())
print(inventory.index.tolist())


# In[6]:


print(inventory.dtypes)


# In[7]:


print(inventory.isnull().sum())


# In[8]:


print(inventory.loc["Product3"])


# In[9]:


print(inventory["Location2"])


# In[10]:


print(inventory.loc[["Product1", "Product4"], ["Location1", "Location3"]])


# In[11]:


print(inventory.iloc[:3, :2])


# In[12]:


print(inventory.at["Product5", "Location3"])


# In[13]:


inventory.at["Product2", "Location4"] = 120
print(inventory)


# In[14]:


inventory.loc["Product6"] = [150, 180, 140, 200]
print(inventory)


# In[15]:


inventory += 10
print(inventory)


# In[16]:


inventory.loc["Product4"] -= 5
print(inventory)


# In[17]:


stock_percentage = (inventory / 1000) * 100
print(stock_percentage)


# In[18]:


print(inventory.sum(axis=1))


# In[21]:


print(inventory.sum(axis=0))


# In[20]:


print(inventory.sum(axis=1).idxmax())


# In[22]:


print(inventory.sum(axis=0).idxmin())


# In[23]:


print(inventory.mean())


# In[24]:


inventory["Total Stock"] = inventory.sum(axis=1)
print(inventory)


# In[25]:


inventory = inventory.sort_values(by="Total Stock", ascending=False)
print(inventory)


# In[26]:


filtered_inventory = inventory[inventory["Total Stock"] > 1000]
print(filtered_inventory)

