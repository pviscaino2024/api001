from sqlalchemy import column, Integer,String,DateTime
from database import Base 
class Persona(Base):
    __tablename__= "Persona"
    id= Column(Integer, primary_key = true, autoincrement= true)