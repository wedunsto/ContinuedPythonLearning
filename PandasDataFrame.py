#Objective: Dive deeper into Pandas DataFrame

import pandas as pd #Import needed to work with Pandas

DataFrameData = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv") #Create Pandas DataFrame from a URL
FirstTenRows = DataFrameData.head(10) #Stores first 10 rows
print(FirstTenRows,"\n\n")

BottomTenRows = DataFrameData.tail(10) #Stores bottom 10 rows
print(BottomTenRows,"\n\n")

FirstFourColNames = list(DataFrameData)[:4] #Stores first 4 column names
FirstFourCols = DataFrameData.iloc[:4,:4] #Stores first 4 rows and first four columns
#Use .iloc[] / loc[] when possible. Using df[] can cause warning errors
print(FirstFourCols,"\n\n")

SummaryData = DataFrameData.describe(); #Stores a analytical DataFrame
print(SummaryData,"\n\n")

States = ['CA','WA','MA','NC'] #Stores the values for the new column
FirstFourCols["States"] = States #Creates a new column with the column values
print("Add Column Example:","\n",FirstFourCols,"\n\n")

DeleteCols = ["Team", "Number"] #Stores column names to be deleted
FirstFourCols.drop(DeleteCols,axis = 1, inplace = True) #Deletes to the columns
print("Delete Column Example:","\n",FirstFourCols,"\n\n")

RowValues = {"Name":"William Dunston","Position":"WR","States":"NC"} #Stores the values for the new row
NewRow = pd.DataFrame(RowValues,index=[0]) #Create a 1 row DataFrame
FirstFourCols = pd.concat([NewRow,FirstFourCols]).reset_index(drop=True) #Concatenate FirstFourCols and NewRow
print("Add Row Example:","\n",FirstFourCols,"\n\n")

DeleteRows = [2] #Stores the row index(es) to be deleted
FirstFourCols.drop(DeleteRows,inplace = True)
print("Delete Row Example:","\n",FirstFourCols,"\n\n") #Deletes the row(s) from the DataFrame

TruncateDataFrameData = DataFrameData.truncate(before = 5, after = 9) #Only displays rows after 5th row and before 9th row
TruncateColumns = list(TruncateDataFrameData) #Store all columns
TruncateDataFrameData = TruncateDataFrameData[TruncateColumns[:4]] #Only use the first 4 columns
print("Truncation Example:","\n",TruncateDataFrameData,"\n\n")

TruncateDataFrameData.sort_values("Number", axis = 0, ascending = True, inplace = True) #Sort DataFrame by the player number in ascending order
print("Sorting Example: \n",TruncateDataFrameData,"\n\n")

GroupTeams = DataFrameData.groupby("Team") #Group DataFrame by Teams
GroupTeamsSum = GroupTeams.sum() #Sums up numerical values in the groups
print("Summed Up Group Values \n",GroupTeamsSum,"\n\n")

GroupTeamsAndNumber = DataFrameData.groupby(["Team","Number"]) #Group DataFrame by Teams and Numbers

print("Group Loop Example (3x3 for space): ")
for teams, group in GroupTeams: #Loop through all the team groups
    print(teams) #Loop teams (string)
    print(group.iloc[:3,:3],"\n") #Loop group values (dataframe)
    
print("Group Select Example (3x3 for space): ")
BrooklynNets = GroupTeams.get_group("Brooklyn Nets").iloc[:3,:3] #Grabs the first 3 entries in the Brooklyn Nets group
print(BrooklynNets)