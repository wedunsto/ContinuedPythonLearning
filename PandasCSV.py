#Objective: Introduce working with Pands and csv files
#Opening and saving csv files

import numpy as np
import pandas as pd

df = pd.read_csv("Sports.csv",index_col="Brand") #Saves the csv file as a DataFrame
#Sets the index to the brands
print(df,"\n\n")

BoardsSeries = pd.read_csv("Sports.csv",usecols=["Brand"], squeeze = True) #Save only the column Brand from the CSV as a Series
print(BoardsSeries,"\n\n")

Newdf = pd.read_csv("Sports.csv",index_col="Brand",skiprows=[1]) #Saves the csv file as a Dataframe, skipping the second row
print(Newdf,"\n\n")

df["Event"] = ["Super pipe", "Half pipe"] #Create a new DataFrame with a new column
EditedDF = df
print(type(EditedDF),"\n\n")
EditedDF.to_csv('./EditedSports.csv') #Save the edited DataFrame to a new .CSV file