from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from datetime import datetime
from sqlalchemy.orm import declarative_base,sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

database = os.getenv("DATABASE_URL")

engine = create_engine(database)

sessionLocal = sessionmaker(bind = engine)

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key= True, index = True)
    email = Column(Text, nullable = False)
    password = Column(Text, nullable = False)

class Manuals(Base):
    __tablename__ = "manuals"
    id = Column(Integer, primary_key = True, index = True)
    user_id = Column(Integer)
    filename = Column(String)
    upload_date = Column(DateTime, default= datetime.utcnow)

class ChatHistory(Base):
    __tablename__ = "chat_history"
    id = Column(Integer, primary_key = True, index = True)
    user_id = Column(Integer)
    manuals_id = Column(Integer)
    question = Column(Text)
    answer = Column(Text)
    time_stamp = Column(DateTime, default = datetime.utcnow)

Base.metadata.create_all(bind=engine)


def add_user(email:str, password:str):
    session = sessionLocal()
    user = User(email = email, password = password)
    session.add(user)
    session.commit()
    session.close()

def add_manuals(user_id:int, filename:str):
    session = sessionLocal()
    manuals = Manuals(user_id = user_id, filename = filename)
    session.add(manuals)
    session.commit()
    session.close()

def add_chat(user_id:int, manuals_id:int, question:str, answer:str):
    session = sessionLocal()
    chat = ChatHistory(user_id = user_id, manuals_id = manuals_id, question = question, answer = answer)
    session.add(chat)
    session.commit()
    session.close()

def get_user(email:str):
    session = sessionLocal()
    record = session.query(User).filter(User.email == email).first()
    session.close()
    return record
