'''                                 ***Entertainer- Last Work***
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

fp1="C:/Users/aashl/OneDrive/Desktop/project 1/Entertainer - Last work Info.xlsx"
data1= pd.read_excel(fp1,0)

print(data1.info())
data_cleaned=data1.dropna()
print(data1.head())
print('The non-null values of the given table can be represented as\n:', data_cleaned)

plt.figure(figsize=(11,6))
sns.histplot(data1['Year of Last Major Work (arguable)'] , color='#b411e8')
plt.title("Histplot")
plt.xlabel('Year of Last Major Work (arguable)')
plt.show()

'''Summary of Year of Last Major Work Analysis
From the histogram and data analysis, it is clear that the year 2016 has the highest number of occurrences,
with a total count of 30.

This observation suggests that 2016 was a significant year for many entertainers in terms of their last
notable contributions to their careers.'''

print(data1['Year of Last Major Work (arguable)'].value_counts())
print(data1['Year of Last Major Work (arguable)'].value_counts().index[0])             

rep_values = pd.Series(index=['Year of Last Major Work (arguable)', 'Year of Death'],data=[data1['Year of Last Major Work (arguable)'].mean(), data1['Year of Death'].mean()])
print(rep_values)

'''After careful and intensive analysis of all the given entertainer datasets, we come to the
following Final conclusions:
    1.From the given data, we can use simple visualisations to get a sense of how data is distributed.

    2.We can use various measures of central tendency (Mean,Median,Mode) to represent a group of observations.

    3.The type of central tendency measure to use depends on the type and distribution of the data.
'''



