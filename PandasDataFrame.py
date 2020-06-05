#Objective: Dive deeper into Pandas DataFrame

import pandas as pd

DataFrameData = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv") #Create Pandas DataFrame from a URL
FirstTenRows = DataFrameData.head(10) #Stores first 10 rows
print(FirstTenRows,"\n\n")

BottomTenRows = DataFrameData.tail(10) #Stores bottom 10 rows
print(BottomTenRows,"\n\n")

FirstFourColNames = list(DataFrameData)[:4] #Stores first 4 column names
FirstFourCols = DataFrameData[FirstFourColNames] #Stores first 4 columns
print(FirstFourCols,"\n\n")

SummaryData = DataFrameData.describe(); #Stores a analytical DataFrame
print(SummaryData,"\n\n")

SubSetData = FirstFourCols.head(4); #Stores the first 4 rows and columns 
print(SubSetData,"\n\n")

States = ['CA','WA','MA','NC'] #Stores the values for the new column
SubSetData["States"] = States #Creates a new column with the column values
print("Add Column Example:","\n",SubSetData,"\n\n")

DeleteCols = ["Team", "Number"] #Stores column names to be deleted
SubSetData.drop(DeleteCols,axis = 1, inplace = True) #Deletes to the columns
print("Delete Column Example:","\n",SubSetData,"\n\n")

RowValues = {"Name":"William Dunston","Position":"WR","States":"NC"} #Stores the values for the new row
NewRow = pd.DataFrame(RowValues,index=[0]) #Create a 1 row DataFrame
SubSetData = pd.concat([NewRow,SubSetData]).reset_index(drop=True) #Concatenate SubSetData and NewRow
print("Add Row Example:","\n",SubSetData,"\n\n")

DeleteRows = [2] #Stores the row index(es) to be deleted
SubSetData.drop(DeleteRows,inplace = True)
print("Delete Row Example:","\n",SubSetData,"\n\n") #Deletes the row(s) from the DataFrame

TruncateDataFrameData = DataFrameData.truncate(before = 5, after = 9) #Only displays rows after 5th row and before 9th row
TruncateColumns = list(TruncateDataFrameData) #Store all columns
TruncateDataFrameData = TruncateDataFrameData[TruncateColumns[:4]] #Only use the first 4 columns
print("Truncation Example:","\n",TruncateDataFrameData,"\n\n")

TruncateDataFrameData.sort_values("Number", axis = 0, ascending = True, inplace = True) #Sort DataFrame by the player number in ascending order
print("Sorting Example: \n",TruncateDataFrameData,"\n\n")

