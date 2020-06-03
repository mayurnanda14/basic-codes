# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
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

