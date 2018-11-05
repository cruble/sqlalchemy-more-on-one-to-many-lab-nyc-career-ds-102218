from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()


# write the Player, City, Sport and Team tables below
class Player(Base):
	__tablename__ = "players"

	id = Column(Integer, primary_key=True)
	name = Column(Text)
	age = Column(Integer)
	number = Column(Integer)
	height = Column(Text)
	weight = Column(Integer)
	birthday = Column(String)
	team_id = Column(Integer, ForeignKey('teams.id'))
	team = relationship('Team', back_populates='players')

class Team(Base):
	__tablename__ = "teams"

	id = Column(Integer, primary_key=True)
	name = Column(Text)


	city_id = Column(Integer, ForeignKey('cities.id'))
	city = relationship('City', back_populates='teams')

	sport_id = Column(Integer, ForeignKey('sports.id'))
	sport = relationship('Sport', back_populates='teams')

	players = relationship(Player, back_populates='team')




class Sport(Base):
	__tablename__ = 'sports'

	id = Column(Integer, primary_key=True)
	name = Column(Text)

	teams = relationship(Team, back_populates='sport')


class City(Base):
	__tablename__ = 'cities'

	id = Column(Integer, primary_key=True)
	name = Column(Text)
	state = Column(Text)

	teams = relationship(Team, back_populates='city')



engine = create_engine('sqlite:///sports.db')
Base.metadata.create_all(engine)
