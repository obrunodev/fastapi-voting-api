from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, UniqueConstraint
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

# Cria a base declarativa para os modelos
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    # Relação com a tabela de votos
    votes = relationship("Vote", back_populates="voter")


class Movie(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True)
    description = Column(String)

    # Relação com a tabela de votos
    votes = relationship("Vote", back_populates="movie")


class Vote(Base):
    __tablename__ = 'votes'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    movie_id = Column(Integer, ForeignKey('movies.id'))
    timestamp = Column(DateTime, default=datetime.utcnow)

    # Relação com as tabelas de User e Movie
    voter = relationship("User", back_populates="votes")
    movie = relationship("Movie", back_populates="votes")

    # Garante que um usuário só vote uma vez por filme
    __table_args__ = (UniqueConstraint('user_id', 'movie_id', name='_user_movie_uc'),)
