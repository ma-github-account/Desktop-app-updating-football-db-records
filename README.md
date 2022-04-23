This desktop application allows to upload football (soccer) player information into the database.
User fills the form and clicks "upload_to_database" button.

Prerequisites:
- Python 3.9.7
- tkinter
- pyodbc

We are uploading the player information into database:

CREATE TABLE [dbo].[Football_Player](
	[FirstName] [varchar](50) NOT NULL,
	[LastName] [varchar](50) NOT NULL,
	[Height] [int] NOT NULL,
	[Age] [int] NOT NULL,
	[Club] [varchar](50) NOT NULL,
	[Position] [varchar](50) NOT NULL,
	[ContractLength] [int] NOT NULL,
	[OnLoan] BIT NOT NULL,
	[Country] [varchar](50) NOT NULL,
	[GamesforNationalTeam] [int] NOT NULL,
	[GoalsforNationalTeam] [int] NOT NULL,
	[AgentName] [varchar](50) NOT NULL,
	[TransferValue] [int] NOT NULL,
	[TransferListStatus] [varchar](50) NOT NULL
	)





![app_screen](https://user-images.githubusercontent.com/89083426/164913689-0aedb1ef-d98f-4750-be36-6ed3d65ac52b.png)

![db_result](https://user-images.githubusercontent.com/89083426/164913695-1ceb247f-074a-4413-896d-b7d1dabbcd2b.png)


