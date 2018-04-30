
# coding: utf-8

# In[43]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[44]:


import csv
import numpy
import json
from wordcloud import WordCloud
import matplotlib.pyplot as plt


# In[117]:


#json_filename = 'jsondata\A_Series_of_Unfortunate_Events_hist.json'

csv_filename = 'csvdata\A_Series_of_Unfortunate_Events_hist_all.csv'
#don't forget "\\" after output_path
output_path = 'D:\study\social network data mining\wordcloud\word-cloud-program\output' + '\\'
output_name = 'A_Series_of_Unfortunate_Events_hist_all'


# In[118]:


data = []
with open(csv_filename, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        data.append(row)


# In[119]:


json_data = json.dumps(data)


# In[120]:


#print(json_data)


# In[121]:


#read json
#with open(json_filename,  encoding='utf-8') as jsonfile:
#    data = json.load(jsonfile)


# In[122]:


#print(data)


# In[123]:


text = ""


# In[124]:


# get dictonary by json
dictdata = {}
for d in data:
    dictdata[d['Data']] = d[' Value']


# In[125]:


#print(dictdata)


# In[126]:


# get text from duplicating word by dictonary
for word, dup in dictdata.items():
    #print(word)
    #print(dup)
    for i in range(int(dup)):
        text = text + word + " "


# In[127]:


#print(text)


# In[128]:


#get word cloud by text 
wordcloud = WordCloud(width=3200, height=1600, prefer_horizontal=1, font_step=5, min_font_size=4, background_color="white").generate(text)


# In[129]:


# get image by word cloud
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
image = wordcloud.to_image()
image.show()
image.save(output_path + output_name + '.BMP')

