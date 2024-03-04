

from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from contextvars import ContextVar
from dotenv import load_dotenv
import os

load_dotenv()  # take environment variables from .env.
HOST = os.environ.get("DB_DEFAULT_HOSTNAME")
PORT = os.environ.get("DB_DEFAULT_PORT")
USERNAME = os.environ.get("DB_DEFAULT_USERNAME")
PASS = os.environ.get("DB_DEFAULT_PASSWORD")
DBNAME = os.environ.get("DB_DEFAULT_DATABASE_NAME")

URL = "mysql+pymysql://"+USERNAME+":"+PASS+"@"+HOST+":"+PORT+"/"+DBNAME  #beta old server
SQLALCHEMY_DATABASE_URL = URL
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, pool_size=50, max_overflow=0, pool_pre_ping=True, pool_recycle=300
)

meta = MetaData()
conn = engine.connect()
DB_BASE = declarative_base()
SessionLocal = sessionmaker(bind= engine, autocommit=False, autoflush=False)

# print (conn)

async def get_db():
    
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

