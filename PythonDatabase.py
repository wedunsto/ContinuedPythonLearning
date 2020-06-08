#import pymysql as pm #Import necessary for MySQL
import PythonDatabaseConnection as dbf #Import necessary to connect to database
import pandas as pd #Import necessary for database
import numpy as np #Import necessary for numpy arrays

Host = 'localhost' #Name of the database host
User = 'root' #Username for connecting to the host
Pass = 'test' #Password for User to connect to the host
Database = 'nba_players' #Name of database on the host

dbf.ConnectToDatabase(Host,User,Pass,Database) #Calls the database connection function

Column_Header = dbf.DatabaseColumns()#Call the column header function

Rows = dbf.DatabaseQuery("Select * From nba") #Calls the database query function

df = pd.DataFrame(Rows) #Use the rows list to build a dataframe
print(df.iloc[0])