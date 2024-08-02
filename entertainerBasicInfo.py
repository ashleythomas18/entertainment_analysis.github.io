'''                                 ******Entertainer Data Analytics******

Sheet 1: Entertainer - Basic Data

The dataset comprises 70 rows and 3 columns, with each row representing an entertainer. The columns include:
Name: The name of the actor or actress
Gender: The gender of the entertainer
Birth Year: The year of birth of the entertainer

Dataset Features:
Given the limited number of features in this dataset, we primarily focus on visualizing the birth year data to derive insights. To illustrate these observations, we will plot a histogram of the birth year data.
insights.
'''


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

fp = "C:/Users/aashl/OneDrive/Desktop/project 1/Entertainer - Basic Info.xlsx"

data = pd.read_excel(fp,0)

print('The first few rows of the given dataset can be viewed by:', data.head())
#print(data.isnull().sum())
data = data.dropna()             #used to remove the null values from a table
print(data.shape)                #indicates the number of rows and columns
print(data.index)                #the number of indices, for example: (0-69)(70 values)
print(data.columns)              #the total number of columns
print(data.info())               #briefs us about the datatype and and the total amount of memory used.
print(data.dropna())

'''
To illustrate these observations, we will plot a histogram of the birth year data.
'''

plt.figure(figsize=(11,6))
sns.histplot(data=data, x='Birth Year', color='orange', edgecolor='linen', alpha=0.5, bins=5)
plt.title('Distribution of basic info')
plt.xlabel('Birth Year')
plt.ylabel('Gender (traditional)')
plt.show()

'''
Observations:
Upon analyzing the birth year distribution, the following trends are observed:

    1.The majority of actors and actresses were born in the year 1940, followed by notable numbers in 1900 and 1960.
'''



