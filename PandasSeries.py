import numpy as np
import pandas as pd

Data = np.array([1,2,3,4]) #Numpy array for Pandas Series
ResultData = pd.Series(Data) #Pandas Series based on Numpy array

print(ResultData.iloc[:2],"\n\n") #Only access the first 2 elements in the Series

NewResultData = pd.Series(Data,index = ["Skateboards","Snowboards","Longboards","FPGAs"]) #Create a new Pandas Series with defined indexes
print(NewResultData.loc["FPGAs"],"\n\n") #Access value at index 

file = pd.read_csv('Sports.csv',index_col="Brand") #Read in csv with Brand column acting as index
SeriesData = pd.Series(file["Sponsor"]) #Create Series based on Sponsor column
print(SeriesData.loc["Burton"],"\n\n") #Access Sponsor value at the Burton index

NewData = np.array([1,2,3,4,5,6,7,8,9,0]) #Numpy array for Pandas Series
SeriesData0 = pd.Series(NewData[:5], index = ['A','B','C','D','E']) #Create a Series with indexes
SeriesData1 = pd.Series(NewData[5:], index = ['F','G','H','I','J']) #Create a Series with indexes

SeriesData2= SeriesData1.add(SeriesData0,fill_value = 0) #Adds values with the same indexes together

print(SeriesData2)