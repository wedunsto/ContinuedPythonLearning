#Objective: Practice and introduce Pandas and Numpy
#Introduce DataFrames

import numpy as np
import pandas as pd

Data = np.array(['Microcontroller','FPGA','Android Devices']) #Numpy array to be converted into a series
SeriesData = pd.Series(Data) #Creates a series based on the data array

print(SeriesData,"\n\n") #Print the Column Series

Values = np.array([[1,2,3],[2,3,4],[4,5,6]]) #Create a Numpy array for the values in the DataFrame
Index = np.array(['System 1','System 2','System 3'])#Numpy array to hold index values
DataFrameData = pd.DataFrame(Values, index= Index, columns = Data) #Create DataFrame based on the Numpy arrays

print(DataFrameData,"\n\n\n") #Print the entire DataFrame
print(DataFrameData["Microcontroller"],"\n\n") #Prints the Indexes and Values of the Microcontroller column
print(DataFrameData.loc["System 2"],"\n\n") #Prints the Columns and Values of the System 2 index
print(DataFrameData.iloc[2],"\n\n") #Prints the Columns and Values of the System 3 index

NewValues = np.array([[1,2,3],[2,3,4],[4,5,6],[np.nan, np.nan, np.nan]]) #Adds NULL values to Numpy array
NewIndex = np.array(['System 1','System 2','System 3', 'System 4'])#Numpy array to hold index values
NewDataFrameData = pd.DataFrame(NewValues, index= NewIndex, columns = Data) #Create DataFrame based on the Numpy arrays
print(NewDataFrameData.isnull(),"\n\n") #Determines if a cell is null or not

FixedDataFrameData = NewDataFrameData.fillna(0) #Create a DataFrame with no NaN values
print(FixedDataFrameData,"\n\n")
ReducedDataFrameData = NewDataFrameData.dropna() #Create a DataFrame where every row with an NaN value is removed
print(ReducedDataFrameData,"\n\n")

for rows, columns in DataFrameData.iterrows(): #Prints all values in every row
    print(rows,"\n",columns)
    print()
    
print("\n\n")
    
Columns = list(DataFrameData) #Create a list of DataFrame columns
for column in Columns: #Loop through DataFrame columns
    print(column," : ",DataFrameData[column][0]) #Prints all values in the first row with associated column