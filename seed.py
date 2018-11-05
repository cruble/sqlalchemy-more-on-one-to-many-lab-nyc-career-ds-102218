from models import *
from sqlalchemy import create_engine
import pandas as pd
import pdb
import datetime 

engine = create_engine('sqlite:///sports.db')

Session = sessionmaker(bind=engine)
session = Session()

# below we are reading the csv files to create the data we will need to create the players
# pandas returns a DataFrame object from reading the CSV
# we then tell the DataFrame object to turn each row into dictionaries
# by giving to_dict the argument "orient='records'"
# we are telling our DataFrame to make each row a dictionary using the column headers
# as the keys for the key value pairs in each new dictionary
# feel free to uncomment lines 18-21 to see each step of the process in your terminal
# ____ example ______
# la_dodgers0 = pd.read_csv('la_dodgers_baseball.csv')
# la_dodgers1 = pd.read_csv('la_dodgers_baseball.csv').to_dict()
# la_dodgers2 = pd.read_csv('la_dodgers_baseball.csv').to_dict(orient='records')

# __________________
la_dodgers = pd.read_csv('la_dodgers_baseball.csv').to_dict(orient='records')
la_lakers = pd.read_csv('la_lakers_basketball.csv').to_dict(orient='records')
ny_yankees = pd.read_csv('ny_yankees_baseball.csv').to_dict(orient='records')
ny_knicks = pd.read_csv('ny_knicks_basketball.csv').to_dict(orient='records')


# now that we have the data for each player
# add and commit the players, teams, sports and cities below
# we will need to probably write at least one function to iterate over our data and create the players
# hint: it may be a good idea to creat the Teams, Cities, and Sports first 

ny = City(name="New York", state="New York")
la = City(name="Los Angeles", state="California")

dodgers = Team(name ="Dodgers")
yankees = Team(name ="Yankees")
knicks = Team(name = "Knicks")
lakers = Team(name = "Lakers")

basketball = Sport(name = "basketball")
baseball = Sport(name = "baseball")

dodgers.city = la 
yankees.city = ny 
knicks.city = ny 
lakers.city = la 

dodgers.sport = baseball 
yankees.sport = baseball
knicks.sport = basketball
lakers.sport = basketball

# pdb.set_trace()
session.add_all([ny, la, dodgers, yankees, knicks, lakers, basketball, baseball])
session.commit() 

now = datetime.date.today()
commit_list = []

for dodger in la_dodgers: 
	bday = dodger['birthdate']
	bday_list = bday.split('/')
	year = bday_list[2]
	if len(year) < 4:
		year = "19" + year 
	bday_date = datetime.date(int(year), int(bday_list[0]), int(bday_list[1]))
	age = now.year - bday_date.year  

	new_dodger = Player(name = dodger['name'], number = dodger['number'] , height = dodger['height'], weight = dodger['weight'], age = age)
	new_dodger.team = dodgers
	commit_list.append(new_dodger)
	session.add(new_dodger)
	session.commit()

for yankee in ny_yankees: 
	new_yankee = Player(name = yankee['name'], height = yankee['height'], weight = yankee['weight'], age = yankee['age'])
	new_yankee.team = yankees 
	commit_list.append(new_yankee)
	session.add(new_yankee)
	session.commit()

for knick in ny_knicks: 
	new_knick = Player(name = knick['name'], height = knick['height'], weight = knick['weight'], age = knick['age'], number = knick['number'])
	new_knick.team = knicks 
	commit_list.append(new_knick)
	session.add(new_knick)
	session.commit()

for laker in la_lakers:
	new_laker = Player(name = laker['name'], height = laker['height'], weight = laker['weight'], age = laker['age'], number = laker['number'])
	new_laker.team = lakers 
	commit_list.append(new_laker)
	session.add(new_laker)
	session.commit()

# session.add_all([commit_list])
# session.commit()











