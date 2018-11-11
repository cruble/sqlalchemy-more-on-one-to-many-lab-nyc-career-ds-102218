from models import *
from sqlalchemy import create_engine

engine = create_engine('sqlite:///sports.db', echo=True)

Session = sessionmaker(bind=engine)
session = Session()

def return_teams_for_new_york():
    # here we want to return all teams that are associated with New York City
    return session.query(City).filter_by(name="New York").all()[0].teams

    # also from solutions
    ## other solution: session.query(City).filter_by(name='New York').first().teams
    ## session.query(Team).join(City).filter(City.name == 'New York').all()

def return_players_for_la_dodgers():
    # here we want to return all players that are associated with the LA dodgers
    return session.query(Team).filter_by(name = "Dodgers").all()[0].players
    # other solution
    # session.query(Player).join(Team).filter(Team.name == 'Dodgers').all()

def return_sorted_new_york_knicks():
    # here we want to return all the players on the New York Knicks
    # sorted in ascending (small -> big) order by their number
    return session.query(Player).join(Team).filter(Team.name == 'Knicks').order_by(Player.number.asc()).all() 
    # return session.query(Player).filter(Player.team_id == knicks.id).order_by(Player.number).all()

def return_youngest_basket_ball_player_in_new_york():
    # here we want to sort all the players on New York Knicks by age
    # and return the youngest player
    return session.query(Player).join(Team).filter(Team.name == "Knicks").order_by(Player.age).first()

def return_all_players_in_los_angeles():
    # here we want to return all players that are associated with
    # a sports team in LA
    # return session.query(Player, Team, City).filter(City == la).all()
    #this gets teams for a city returns a list 
    LA_players = []
    LA_teams = session.query(City).join(Team).join(Player).filter(City.name == "Los Angeles").all()[0].teams
    for team in LA_teams: 
        LA_players.extend(team.players)
    return LA_players 
    # return session.query(Player).join(Team).join(City).filter(City.name == 'Los Angeles')


def return_tallest_player_in_los_angeles():
    # here we want to return the tallest player associted with
    # a sports team in LA
    LA_players = return_all_players_in_los_angeles()
    return max(LA_players, key=lambda x: x.height)
    #  tallest_player = session.query(Player,func.max(Player.height)).join(Team).join(City).filter(City.name=='Los Angeles').first()
    # return tallest_player[0]

def return_team_with_heaviest_players():
    # here we want to return the city with the players that
    # have the heaviest average weight (total weight / total players)
    teams = session.query(Team).all()
    avg_weight_tups = []
    for team in teams:
        team_weight = session.query(Team,func.avg(Player.weight)).filter(Player.team == team ).first()
        avg_weight_tups.append(team_weight)
    heaviest_team = max(avg_weight_tups,key = lambda x: x[1])
    return heaviest_team[0]
