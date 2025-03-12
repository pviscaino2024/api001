from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os 
from dotenv import load_dotenv
load_dotenv()

DB_USER=os.getenv("DB_USER")
DB_PASSWORD=os.getenv("DB_PASSWORD")
DB_HOST=os.getenv("DB_HOST")
DB_NAME= os.getenv("DB_NAME")
DB_PORT= os.getenv("DB_PORT")

URL = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(URL)

sessionlocal = sessionmaker(bind=engine, autoflush=False,expire_oncommit=False)

query = "SELECT * from persona"
db = sessionlocal()
resultado = db.query()