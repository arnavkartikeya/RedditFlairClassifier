#!/usr/bin/env python
# coding: utf-8

# In[8]:


get_ipython().system('pip install fasttext')


# In[46]:


import fasttext

model = fasttext.train_supervised(input="train.txt", lr=1.0, epoch=25, wordNgrams=2)
model.save_model("model_test.bin")
model.test("test.txt")


# In[44]:


import re
def strip_formatting(string):
    string = string.lower()
    string = re.sub(r"([.!?,'/()])", r" \1 ", string)
    string = string.replace("\n", " ")
    return string
def predict(string):
    string = strip_formatting(string)
    print(model.predict(string))


# In[45]:


predict("Why are different wavelengths of light refracted by different amounts?")

