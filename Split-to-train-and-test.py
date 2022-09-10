#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import sys
import random
import numpy as np
import glob
#from glob import glob
import shutil
from tqdm import tqdm
import pathlib


# In[2]:


DATA_DIR = 'H:/Data/Data/uball'
train_dir = f'{DATA_DIR}/trainub'
valid_dir = f'{DATA_DIR}/validub'


# In[3]:


print(train_dir)


# In[4]:


train_fld= glob.glob(train_dir + f'/*')
print(len(train_fld))


# In[5]:


split=0.4


# In[6]:


train_ds = glob.glob(train_dir + f'/2/*.*')
print(train_ds)


# In[7]:


valid_sz = int(split * len(train_ds)) if split < 1.0 else split 


# In[8]:


print(valid_sz)


# In[9]:


valid_ds = random.sample(train_ds, valid_sz)
print(len(valid_ds))


# In[25]:


data_root = pathlib.Path(train_dir)
for item in data_root.iterdir():
    print(item)
    #rain_fld= glob.glob(train_dir + f'/*')
    #train_ds = glob.glob(train_dir + "f'/" + item +"/*.*")
    train_ds = glob.glob(str(item) + f'/*.*')
   
    valid_ds = random.sample(train_ds,valid_sz)
    print(valid_ds)
    #n_test_per_class=max(1,int(len(valid_ds)/len(train_fds)))
    n_train = max(0,len(train_ds)-2)
    n_train_per_class = max(1,int(np.floor(n_train/len(train_fld))))
    n_test_per_class = max(1,int(np.floor(valid_sz/len(train_fld))))
    #valid_mds = #random.sample(train_ds, n_test_per_class)
    for fname in tqdm(valid_ds):
        print(fname)
        basename = os.path.basename(fname)
        label = fname.split('\\')[-2]
        src_folder = os.path.join(train_dir, label)
        tgt_folder = os.path.join(valid_dir, label)
        if not os.path.exists(tgt_folder):
            os.mkdir(tgt_folder)
        shutil.copy(os.path.join(src_folder, basename), os.path.join(tgt_folder, basename))
   
    


# In[ ]:





# In[ ]:





# In[ ]:




