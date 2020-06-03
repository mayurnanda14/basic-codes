# -*- coding: utf-8 -*-
"""
NAN- used as a acronym for Not a number
Created on Sun Mar 22 18:48:23 2020

@author: Mayur

import os
import pandas as pd
import numpy as np
os.chdir('C:/Users/krish/Desktop/mayur/Data Science/Week3')
data=pd.read_csv('Iris_data_sample.csv')
data1=pd.read_csv('Iris_data_sample.csv',index_col=0,na_values=["??","###"])
data2=pd.read_excel('Iris_data_sample.xlsx',sheet_name='Iris_data',index_col=0,na_values=["??","###"])
data3=pd.read_table('Iris_data_sample.txt')   
data4=pd.read_table('Iris_data_sample.txt',sep='\t')      
data5=pd.read_table('Iris_data_sample.txt',delimiter='\t')      
data6=pd.read_table('Iris_data_sample.txt',delimiter=' ',index_col=0,na_values=["??","###"])
cars_data=pd.read_csv('Toyota.csv',index_col=0,na_values=["??","????"])
shallowcopy=cars_data.copy(deep=False) #shallow copy is created i.e changes in copy is also reflected in original data
deepcopy=cars_data.copy(deep=True) #Deep copy is created i.e changes in copy is not reflected in original data
deepcopy.index
deepcopy.columns
deepcopy.size
deepcopy.shape
deepcopy.memory_usage()
deepcopy.ndim
deepcopy.head(6) #returns firt six rows of data-frame
deepcopy.tail(6) #returns last six rows of data-frame
deepcopy.at[4,'FuelType'] #can be used if you are sure about row and column name
deepcopy.iat[7,9]
deepcopy.loc[4:9,['Age','Price','FuelType']]
deepcopy.dtypes
deepcopy.get_dtype_counts()
deepcopy.select_dtypes(exclude=['int64','object'])
deepcopy.info()
np.unique(deepcopy['KM'])
np.unique(deepcopy['HP'])
np.unique(deepcopy['MetColor'])
np.unique(deepcopy['Automatic'])
np.unique(deepcopy['Doors'])
cars_data.info()



import os
import pandas as pd
import numpy as np
os.chdir('C:/Users/krish/Desktop/mayur/Data Science/Week3')
cars_data=pd.read_csv('Toyota.csv',index_col=0,na_values=["??","????"])
cars_data.info() 
cars_data['MetColor']=cars_data['MetColor'].astype('object')
cars_data['Automatic']=cars_data['Automatic'].astype('object')
cars_data.info()
cars_data['FuelType'].nbytes
cars_data['FuelType']=cars_data['FuelType'].astype('category')
cars_data['FuelType'].nbytes
cars_data.info()
cars_data['FuelType']=cars_data['FuelType'].astype('object')
cars_data.info()
cars_data['Doors'].replace('three',3,inplace=True)
cars_data['Doors'].replace('four',4,inplace=True)
cars_data['Doors'].replace('five',5,inplace=True)
cars_data.info() #gives complete information of dataframe i.e memory alloacation, data type of each variable
cars_data['Doors']=cars_data['Doors'].astype('int64') #change type of 'Doors' to integer
cars_data.info()
cars_data.isnull().sum() #gives null values in all columns
cars_data.insert(10,"Price_Class","") 
y=len(cars_data['Price'])

for i in range(y):
  if cars_data['Price'][i]<=8450:
      cars_data['Price_Class'][i]="low"
    elif cars_data['Price'][i]>11950:
        cars_data['Price_Class'][i]="High"
    else:
        cars_data['Price_Class'][i]="Medium"
cars_data.insert(11,"Price1","")
cars_data['Price']

i=0
while i<y:
    if (cars_data['Price'][i])<=8450:
        cars_data['Price_Class'][i]="low"
    elif(cars_data['Price'][i])>11950:
        cars_data['Price_Class'][i]="High"
    else:cars_data['Price_Class'][i]="Medium"
    i=i+1
cars_data['Price_Class'].value_counts() #to get count of unique value in the column

def c_convert(val1,val2):
    val_Converted=val1/12
    ratio=val2/val1
    return[val_Converted,ratio]
        
cars_data['Age_Converted'],cars_data['Km_per_month']=c_convert(cars_data['Age'],cars_data['KM'])
cars_data['Price1']=cars_data['Price']
cars_data['Price_class1']=cars_data['Price_Class']   

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
cars_data1=pd.read_csv('Toyota.csv',index_col=0,na_values=["??","????"])
cars_data2=cars_data1.copy() 
pd.crosstab(index=cars_data2['FuelType'],columns='count',dropna=True)             #to make cross tables_ to see frequency distribution_ to see count of cars of different fuel tupe
pd.crosstab(index=cars_data2['Automatic'],columns=cars_data2['FuelType'],dropna=True)  #to see count of cars of different fuel type and different gear box
pd.crosstab(index=cars_data2['Automatic'],columns=cars_data2['FuelType'],normalize=True,dropna=True)   #to get joint probability
pd.crosstab(index=cars_data2['Automatic'],columns=cars_data2['FuelType'],normalize=True,dropna=True,margins=True) #to get marginal probability
pd.crosstab(index=cars_data2['Automatic'],columns=cars_data2['FuelType'],normalize='index',dropna=True,margins=True) #to get conditional probability with consitions of index
pd.crosstab(index=cars_data2['Automatic'],columns=cars_data2['FuelType'],normalize='columns',dropna=True,margins=True) #to get conditional probability with consitions of columns
numerical_data=cars_data2.select_dtypes(exclude=[object])
print(numerical_data.shape)
corr_matrix=numerical_data.corr()
cars_data3=cars_data1.copy()
cars_data3.dropna(axis=0,inplace=True)
cars_data3.size
cars_data3.shape
plt.scatter(cars_data3['Age'],  cars_data3['Price'],c='red') #scatter plot of Price vs Age
plt.title('Scatter plot of Price vs Age of the cars')
plt.xlabel('Age(months)')
plt.ylabel('Price(Euros)')
plt.show()
plt.hist(cars_data3['KM']) #histogram without bin and color selection
plt.title('Histogram of Kilometer')
plt.xlabel('Kilometer')
plt.ylabel('Frequency')
plt.show()
plt.hist(cars_data3['KM'],color='green',edgecolor='white',bins=5) #histogram with bin and color selection
plt.title('Histogram of Kilometer')
plt.xlabel('Kilometer')
plt.ylabel('Frequency')
plt.show()
count=cars_data3['FuelType'].value_counts()
count1=count.to_frame()
counts=count1['FuelType']
fueltype=('Petrol','Diesel','CNG')
index=np.arange(len(fueltype))
plt.bar(index,counts,color=['red','blue','cyan'])
plt.title('Bar plot for fuel types')
plt.xlabel('fuel types')
plt.ylabel('frequency')
plt.xticks(index,fueltype,rotation=90)
plt.show()
sns.set(style="darkgrid")
sns.regplot(x=cars_data3['Age'],y=cars_data3['Price']) #scatter plot without regression fit line
sns.regplot(x=cars_data3['Age'],y=cars_data3['Price'],fit_reg=False) #scatter plot without regression fit line 
sns.regplot(x=cars_data3['Age'],y=cars_data3['Price'],marker="*",fit_reg=False) #scatter plot without regression fit line and user defined markers
sns.lmplot(x='Age',y='Price',data=cars_data3,fit_reg=False,hue='FuelType',legend=True,palette="Set1") #scatter plot for different fuel type
sns.distplot(cars_data3['Age']) #to give probability distribution of age
sns.distplot(cars_data3['Age'],kde=False) #to give probability distribution of age without kernel density function or probability density function
sns.distplot(cars_data3['Age'],kde=False,bins=5) #to give probability distribution of age without kernel density function or probability density function
sns.countplot(x="FuelType",data=cars_data3) #bar-plot for fuel type for categorical variable
sns.countplot(x="FuelType",data=cars_data3,hue="Automatic") #Grouped bar-plot for fuel type and automatic
sns.boxplot(y=cars_data3["Price"]) #to plot box plot of numerical data of Price
sns.boxplot(x=cars_data3["FuelType"],y=cars_data3["Price"]) #grouped box plot
sns.boxplot(x="FuelType",y="Price",hue="Automatic",data=cars_data3) #grouped box plot with Automatic as hue
f,(ax_box,ax_hist)=plt.subplots(2,gridspec_kw={"height_ratios":(.15,.85)})
sns.boxplot(cars_data3["Price"],ax=ax_box)
sns.distplot(cars_data3["Price"],ax=ax_hist,kde=False)
sns.pairplot(cars_data3,kind="scatter",hue="FuelType")
plt.show()
"""

#DEALING WITH MISSING DATA

import os
import pandas as pd
os.chdir('C:/Users/krish/Desktop/mayur/Data Science/Week3')
cars_data=pd.read_csv('Toyota.csv',index_col=0,na_values=["??","????"])
cars_data.isna().sum()  #to check missing values
cars_data.isnull().sum() #to chech missing values 
missing=cars_data[cars_data.isnull().any(axis=1)]
b=cars_data.describe() #to describe all numerical variables
cars_data['Age'].mean()
cars_data['Age'].fillna(cars_data['Age'].mean(),inplace=True)
cars_data['KM'].median()
cars_data['KM'].fillna(cars_data['KM'].median(),inplace=True)
cars_data['HP'].mean()
cars_data['HP'].fillna(cars_data['HP'].mean(),inplace=True)
cars_data['FuelType'].value_counts()
cars_data['FuelType'].value_counts().index[0] #to get mode of FuelType
cars_data['FuelType'].fillna(cars_data['FuelType'].value_counts().index[0],inplace=True)
cars_data['MetColor'].mode()
cars_data['MetColor'].fillna(cars_data['MetColor'].mode()[0],inplace=True)
cars_data.isnull().sum()    
cars_data1=pd.read_csv('Toyota.csv',index_col=0,na_values=["??","????"])
cars_data1.isnull().sum()
cars_data1=cars_data1.apply(lambda x:x.fillna(x.mean()) if x.dtype=='float' else x.fillna(x.value_counts().index[0]))
cars_data1.isnull().sum()
