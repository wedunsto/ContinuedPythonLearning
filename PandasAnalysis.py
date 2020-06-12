#import pymysql as pm #Import necessary for MySQL
import PythonDatabaseConnection as dbf #Import necessary to connect to database
import pandas as pd #Import necessary for database
import numpy as np #Import necessary for numpy arrays
import datetime as dt #Import datetime to work with time 

Host = 'localhost' #Name of the database host
User = 'root' #Username for connecting to the host
Pass = 'test' #Password for User to connect to the host
Database = 'nba_players' #Name of database on the host

dbf.ConnectToDatabase(Host,User,Pass,Database) #Calls the database connection function

nba_query = "Select * From 'nba'" #Store query 

Column_Header = dbf.DatabaseColumns()#Call the column header function

Rows = dbf.DatabaseQuery("Select * From nba") #Calls the database query function

df = pd.DataFrame(Rows) #Use the rows list to build a dataframe

print("Numeric column")
player_numbers = pd.to_numeric(df[2]) #Convert third column of dataframe to float64
print(player_numbers)

print("Date time column")
dateTime = []
for values in df.iterrows():
    dateTime.append("10/30/1992")
    
df["Date Time"] = dateTime
dateTime = pd.to_datetime(df["Date Time"])
print(dateTime)