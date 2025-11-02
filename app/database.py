from sqlalchemy import create_engine   # type: ignore
from sqlalchemy.orm import sessionmaker # type: ignore
from sqlalchemy.ext.declarative import declarative_base# type: ignore

from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL , echo = True)

sessionlocal =  sessionmaker(bind = engine ,Sautocommit = False ,autoflush = False )

base  = declarative_base()


