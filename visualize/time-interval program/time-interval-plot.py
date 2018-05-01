
# coding: utf-8

# In[132]:


import matplotlib.pyplot as plt


# In[133]:


import csv, json


# In[134]:


import numpy as np


# In[135]:


csv_filename = 'A_Series_of_Unfortunate_Events_time.csv'


# In[136]:


# get data from csv to json
data = []
with open(csv_filename, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',')
    for row in reader:
        data.append(row)
json_data = json.dumps(data)


# In[137]:


# json to list
freq = []
interval = []
for d in data:
    end = d[' End'][1:]
    start = d['Start']
    freq.append(int(d[' Frequently']))
    if (len(interval) == 0):
        interval.append(start)
    interval.append(end)


# In[138]:


# for plot interval at the end of time
freq.append(0)


# In[139]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[140]:


# plot
y = freq
x = np.arange(len(freq))
fig = plt.figure()

#figsize is in inch
plt.figure(num=None, figsize=(12, 8), dpi=80, facecolor='w', edgecolor='k')
plt.xticks(x, interval)

# add text notation
plt.xlabel('Interval')
plt.ylabel('Tweets')
plt.title(csv_filename[:-4])

# plot figure
plt.bar(x, y, width=1, bottom=1, align='edge',linewidth=2)

# save
plt.savefig(csv_filename[:-4] + '.png')

