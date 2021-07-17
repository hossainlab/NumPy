#!/usr/bin/env python
# coding: utf-8

# ## View vs Copy

# When the contents are physically stored in another location, it is called <b>Copy.</b>

# On the other hand, a different view of the same memory content is provided, we call it as <b>View.</b>

# Different array objects can share the same data. NumPy has <b>ndarray.view()</b> method which is a new array object that looks at the same data of the original array.

# Here, change in dimensions of the new array doesn’t change dimensions of the original.

# In[20]:


import numpy as np


# In[50]:


fruits = np.array(["Apple","Mango","Grapes","Watermelon"])


# We will create basket now as a view of fruits

# In[22]:


basket_1 = fruits.view()
basket_2 = fruits.view()


# In[23]:


print(basket_1)
print(basket_2)


# In[24]:


print("ids for the arrays are different.")
print("id for fruits is : ")
print(id(fruits))
print("id for baskets is : ")
print(id(basket_1))
print(id(basket_2))


# In[25]:


basket_1 is fruits


# ##### baskets is a view of the data owned by fruits

# In[26]:


basket_1.base is fruits 


# ### Change a few elements of basket. It changes the elements of fruits

# Here, we assign a new value to the first element of basket_2. You might be astonished that the list of fruits has been "automatically" changed as well. The explanation is that there has been no new assignment to basket_2, only to one of its elements.

# In[27]:


basket_2[0] = "Strawberry"


# In[28]:


basket_2


# In[29]:


fruits


# ##### And this also affects basket_1

# In[31]:


basket_1


# ### Change the entire elements of basket. It does not change fruits

# In[32]:


basket_1 = np.array(["Peach","Pineapple","Banana","Orange"])


# In[33]:


basket_1


# In[34]:


fruits


# In this case, a new memory location had been allocated for basket_1, because we have assigned a complete new list to this variable

# ### Change the shape of basket. It does not change the shape of fruits

# In[38]:


basket_2.shape = 2,2


# In[39]:


print("basket_2: ")
print(basket_2)


# In[40]:


print("Shape of fruits: ")
print(fruits)


# ### Slicing an array returns a view of it

# In[51]:


mini_basket = fruits[2:]


# In[52]:


mini_basket


# In[53]:


fruits[3] = "Peach"


# In[54]:


mini_basket


# In[ ]:





# ## Deep Copy

# The <b>copy()</b> method makes a complete copy of the array and its data, and doesn’t share with the original array.

# In[1]:


import numpy as np


# In[2]:


fruits = np.array(["Apple","Mango","Grapes","Watermelon"])


# We now Create a deep copy of fruits 

# In[3]:


basket = fruits.copy()


# In[4]:


basket


# In[5]:


basket is fruits


# In[6]:


basket.base is fruits  # basket doesn't share anything with fruits


# ### Change contents or shape of bakset. It does not change the contents of fruits

# In[7]:


basket [0] = "Strawberry"


# In[8]:


basket


# In[9]:


fruits


# In[10]:


basket.shape = 2,2


# In[11]:


print("Shape of basket: ")
print(basket)


# In[12]:


print("Shape of fruits: ")
print(fruits)


# In[ ]:




