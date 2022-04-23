
from db_input_management import *
import tkinter as tk
from tkinter import ttk

variables = dict()

root = tk.Tk()
root.title('Player registry input')
root.columnconfigure(0, weight=1)

ttk.Label(
  root,
  text="Player registry input",
  font=("TkDefaultFont", 16)
).grid()

######################
# Player record form #
######################

drf = ttk.Frame(root)
drf.grid(padx=10, sticky=(tk.E + tk.W))
drf.columnconfigure(0, weight=1)


##############################
# Personal Info Frame   #
##############################

p_info = ttk.LabelFrame(drf, text='Personal Information')
p_info.grid(sticky=(tk.W + tk.E))
for i in range(2):
  p_info.columnconfigure(i, weight=1 )

# First Name
variables['First Name'] = tk.StringVar()
ttk.Label(p_info, text='First Name').grid(row=0, column=0)
tk.Entry(
  p_info, textvariable=variables['First Name']
).grid(row=1, column=0, sticky=(tk.W + tk.E))

# Last Name
variables['Last Name'] = tk.StringVar()
ttk.Label(p_info, text='Last Name').grid(row=0, column=1)
tk.Entry(
  p_info, textvariable=variables['Last Name']
).grid(row=1, column=1, sticky=(tk.W + tk.E))

# Height
variables['Height'] = tk.DoubleVar()
ttk.Label(p_info, text="Height (cm)").grid(row=2, column=0)
ttk.Spinbox(
    p_info, textvariable=variables['Height'],
    from_=0, to=250, increment=1,
).grid(row=3, column=0, sticky=(tk.W + tk.E))

# Age
variables['Age'] = tk.DoubleVar()
ttk.Label(p_info, text="Age").grid(row=2, column=1)
ttk.Spinbox(
    p_info, textvariable=variables['Age'],
    from_=0, to=100, increment=1,
).grid(row=3, column=1, sticky=(tk.W + tk.E))

##############################
# Employment Info Frame   #
##############################

e_info = ttk.LabelFrame(drf, text='Employment Information')
e_info.grid(sticky=(tk.W + tk.E))
for i in range(2):
  e_info.columnconfigure(i, weight=1 )

clubs_list = ["Juventus","Inter","AC Milan","AS Roma","Lazio","Cagliari Calcio","AC Fiorentina"]

# Club
variables['Club'] = tk.StringVar()
ttk.Label(e_info, text='Club').grid(row=2, column=0)
ttk.Combobox(
  e_info,
  textvariable=variables['Club'],
  values=clubs_list
).grid(row=3, column=0, sticky=(tk.W + tk.E))

positions_list = ["Goalkeeper","Left Defender","Central Defender","Right Defender","Defensive Midfielder","Left Midfielder","Central Midfielder","Right Midfielder","Offensive Midfielder","Left Winger","Right Winger","Central Forward","Striker"]

# Position
variables['Position'] = tk.StringVar()
ttk.Label(e_info, text='Position').grid(row=2, column=1)
ttk.Combobox(
  e_info,
  textvariable=variables['Position'],
  values=positions_list
).grid(row=3, column=1, sticky=(tk.W + tk.E))

# Contract Lenght (yrs)
variables['Contract Length'] = tk.DoubleVar()
ttk.Label(e_info, text="Contract Length (yrs)").grid(row=4, column=0)
ttk.Spinbox(
    e_info, textvariable=variables['Contract Length'],
    from_=0, to=250, increment=1,
).grid(row=5, column=0, sticky=(tk.W + tk.E))

# On Loan
variables['On Loan'] = tk.BooleanVar(value=False)
ttk.Checkbutton(
  e_info, variable=variables['On Loan'],
  text='On Loan'
).grid(row=5, column=1, sticky=tk.W, pady=5)

##############################
# Country Info Frame   #
##############################

c_info = ttk.LabelFrame(drf, text='Country Information')
c_info.grid(sticky=(tk.W + tk.E))
for i in range(2):
  c_info.columnconfigure(i, weight=1 )

# Country
variables['Country'] = tk.StringVar()
ttk.Label(c_info, text='Country').grid(row=6, column=0)
tk.Entry(
  c_info, textvariable=variables['Country']
).grid(row=7, column=0, sticky=(tk.W + tk.E))

# Games for National Team
variables['Games for National Team'] = tk.DoubleVar()
ttk.Label(c_info, text="Games for National Team").grid(row=8, column=0)
ttk.Spinbox(
    c_info, textvariable=variables['Games for National Team'],
    from_=0, to=250, increment=1,
).grid(row=9, column=0, sticky=(tk.W + tk.E))

# Goals for National Team
variables['Goals for National Team'] = tk.DoubleVar()
ttk.Label(c_info, text="Goals for National Team").grid(row=8, column=1)
ttk.Spinbox(
    c_info, textvariable=variables['Goals for National Team'],
    from_=0, to=250, increment=1,
).grid(row=9, column=1, sticky=(tk.W + tk.E))

##############################
# Transfer Info Frame   #
##############################

t_info = ttk.LabelFrame(drf, text='Transfer Information')
t_info.grid(sticky=(tk.W + tk.E))
for i in range(2):
  t_info.columnconfigure(i, weight=1 )

# Agent Name
variables['Agent Name'] = tk.StringVar()
ttk.Label(t_info, text='Agent Name').grid(row=10, column=0)
tk.Entry(
  t_info, textvariable=variables['Agent Name']
).grid(row=11, column=0, sticky=(tk.W + tk.E))

# Est. Transfer Value
variables['Est. Transfer Value'] = tk.DoubleVar()
ttk.Label(t_info, text="Est. Transfer Value (milion Euro)").grid(row=10, column=1)
ttk.Spinbox(
    t_info, textvariable=variables['Est. Transfer Value'],
    from_=0, to=250, increment=1,
).grid(row=11, column=1, sticky=(tk.W + tk.E))

# Transfer List Status
variables['Transfer List Status'] = tk.StringVar()
ttk.Label(t_info, text='Transfer List Status').grid(row=12, column=0)
labframe = ttk.Frame(t_info)
for lab in ('Not for sale', 'On transfer list', 'On loan list'):
  ttk.Radiobutton(
    labframe, value=lab, text=lab, variable=variables['Transfer List Status']
).pack(side=tk.LEFT, expand=True)
labframe.grid(row=13, column=0, sticky=(tk.W + tk.E))

########################
# Save & Reset Buttons #
########################

buttons = ttk.Frame(drf)
buttons.grid(sticky=tk.E + tk.W)
upload_button = ttk.Button(buttons, text='Upload to database')
upload_button.pack(side=tk.RIGHT)

reset_button = ttk.Button(buttons, text='Reset')
reset_button.pack(side=tk.LEFT)

##############
# Status Bar #
##############

status_variable = tk.StringVar()
ttk.Label(
  root, textvariable=status_variable
).grid(sticky=tk.W + tk.E, row=99, padx=10)

#############
# Functions #
#############

def on_reset():

  for variable in variables.values():
    if isinstance(variable, tk.BooleanVar):
      variable.set(False)
    else:
      variable.set('')

reset_button.configure(command=on_reset)

def upload_to_database():

	FirstName = variables['First Name'].get()
	LastName = variables['Last Name'].get()
	Height = variables['Height'].get()
	Age = variables['Age'].get()
	Club = variables['Club'].get()
	Position = variables['Position'].get()
	ContractLength = variables['Contract Length'].get()
	OnLoan = variables['On Loan'].get()
	Country = variables['Country'].get()
	GamesforNationalTeam = variables['Games for National Team'].get()
	GoalsforNationalTeam = variables['Goals for National Team'].get()
	AgentName = variables['Agent Name'].get()
	TransferValue = variables['Est. Transfer Value'].get()
	TransferListStatus = variables['Transfer List Status'].get()

	insert_player_into_database(FirstName, LastName, Height, Age, Club, Position, ContractLength, OnLoan, Country, GamesforNationalTeam, GoalsforNationalTeam, AgentName, TransferValue, TransferListStatus)

upload_button.configure(command=upload_to_database)

on_reset()

root.mainloop()














