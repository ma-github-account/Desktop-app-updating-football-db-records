
import pyodbc

server = "db_server"
database = "database"
username = "username"
password = "password"

cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

cursor = cnxn.cursor()

def insert_player_into_database(FirstName, LastName, Height, Age, Club, Position, ContractLength, OnLoan, Country, GamesforNationalTeam, GoalsforNationalTeam, AgentName, TransferValue, TransferListStatus):

	count = cursor.execute("""
	INSERT INTO Football_Player (FirstName, LastName, Height, Age, Club, Position, ContractLength, OnLoan, Country, GamesforNationalTeam, GoalsforNationalTeam, AgentName, TransferValue, TransferListStatus) 
	VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
	FirstName, LastName, Height, Age, Club, Position, ContractLength, OnLoan, Country, GamesforNationalTeam, GoalsforNationalTeam, AgentName, TransferValue, TransferListStatus).rowcount

	cnxn.commit()















