import pymysql as pm #Import necessary for MySQL

print("ConnectToDatabase(Hostname, Username, Password, Database) : Connect to database","\n")
print("DatabaseColumns() : Returns all the column names in a tuple","\n")
print("DatabaseQuery(Query): Returns results of any query in a list","\n")

def ConnectToDatabase(Host,User,Pass,Database):
        global Connection; #Create global variable Connection
        Connection = pm.connect(Host,User,Pass,Database) #Establish connection to the database
        if Connection.open: #Confirm database connection
            print("Successfully connected to the database","\n\n")
            
def DatabaseColumns():
    with Connection.cursor() as Traverse: #Traverse records from the result set
        Traverse.execute("SELECT column_name FROM information_schema.columns WHERE table_schema = 'nba_players' AND table_name = 'nba'") #Execute the described query
        return Traverse.fetchall() #Store all the results in a tuple
    
def DatabaseQuery(Query):
    with Connection.cursor() as Traverse: #Traverse records from the result set
        Traverse.execute(Query) #Excutes the described query
        return list(Traverse.fetchall()) #Stores all the results in a list called rows