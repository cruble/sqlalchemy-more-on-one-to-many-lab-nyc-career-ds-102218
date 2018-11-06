from models import *
from sqlalchemy import create_engine

engine = create_engine('sqlite:///sports.db')

Session = sessionmaker(bind=engine)
session = Session()

def return_teams_for_new_york():
    # here we want to return all teams that are associated with New York City
    return session.query(Team).filter(team.city_id == ny.id).all()

def return_players_for_la_dodgers():
    # here we want to return all players that are associated with the LA dodgers
    return session.query(Player).filter(Player.team_id == dodgers.id).all()

def return_sorted_new_york_knicks():
    # here we want to return all the players on the New York Knicks
    # sorted in ascending (small -> big) order by their number
    return session.query(Player).filter(Player.team_id == knicks.id).order_by(Player.number).all()

def return_youngest_basket_ball_player_in_new_york():
    # here we want to sort all the players on New York Knicks by age
    # and return the youngest player
    return session.query(Player).filter(Player.team_id == knicks.id).order_by(Player.age).first()

def return_all_players_in_los_angeles():
    # here we want to return all players that are associated with
    # a sports team in LA
    # return session.query(Player, Team, City).filter(City == la).all()
    pass 

def return_tallest_player_in_los_angeles():
    # here we want to return the tallest player associted with
    # a sports team in LA
    pass

def return_team_with_heaviest_players():
    # here we want to return the city with the players that
    # have the heaviest average weight (total weight / total players)
    player = 
    pass
