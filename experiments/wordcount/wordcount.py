#!/usr/bin/python
import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

filename=sys.argv[1]
excludefilename=sys.argv[2]
file = open(filename,"r+")
excludefile = open(excludefilename,"r+")
excludewords =[]

for word in excludefile.read().split():
	excludewords.append(word)

wordcount={}
for word in file.read().split():
        if word not in excludewords:
		if word not in wordcount:
			wordcount[word] = 1
		else:
			wordcount[word] = wordcount[word] +1
file.close()
excludefile.close()
dataFrame=pd.DataFrame(wordcount.items())
dataFrame = dataFrame.rename(columns={0:'word', 1:'count'})
dataFrame['perc'] = dataFrame['count']/(dataFrame['count'].sum())*100
dataFrame = dataFrame.sort_values(by = 'perc', ascending = False)

print dataFrame
selectedwords = dataFrame['word'][:10]
axis = np.arange(len(selectedwords))
freqdata = dataFrame['count'][:10]
plt.bar(axis, freqdata,color='green', align='center')

plt.xticks(axis, selectedwords, rotation = 45, fontsize = 10)

plt.xlabel('Word')
plt.ylabel('count')
plt.title('Top 10 Words')

plt.show()

#print (dataFrame)
