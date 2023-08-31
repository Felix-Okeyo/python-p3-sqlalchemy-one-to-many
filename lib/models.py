# Import necessary modules from SQLAlchemy
from sqlalchemy import ForeignKey, Column, Integer, String, MetaData
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

# Define a naming convention for foreign keys
convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}

# Create a metadata object with the defined naming convention
metadata = MetaData(naming_convention=convention)

# Create a base class for declarative models with the defined metadata
Base = declarative_base(metadata=metadata)

# Define a class representing the "Game" table
class Game(Base):
    # Table name
    __tablename__ = 'games'
    
    # Columns of the table
    id = Column(Integer(), primary_key=True)
    title = Column(String())
    genre = Column(String())
    platform = Column(String())
    price = Column(Integer())
    
    # Define a one-to-many relationship between Game and Review
    reviews = relationship('Review', backref=backref('game'), cascade='all, delete-orphan')
    
    # Define a string representation for the Game class
    def __repr__(self):
        return f'Game(id={self.id}, ' + \
            f'title={self.title}, ' + \
            f'platform={self.platform})'

# Define a class representing the "Review" table
class Review(Base):
    # Table name
    __tablename__ = 'reviews'
    
    # Columns of the table
    id = Column(Integer(), primary_key=True)
    score = Column(Integer())
    comment = Column(String())
    
    # Define a foreign key relationship to the Game table
    game_id = Column(Integer(), ForeignKey('games.id'))
    
    # Define a string representation for the Review class
    def __repr__(self):
        return f'Review(id={self.id}, ' + \
            f'score={self.score}, ' + \
            f'game_id={self.game_id})'
