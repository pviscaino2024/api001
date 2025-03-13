from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import sessionlocal
from models import Persona, Localidad, AdminAyuda, Registro, RegistroLogin
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

def get_db():
    db = sessionlocal()
    try:
        yield db
    #except Exception as e:
        # print(e.) sirve para imprimir
    finally:
        db.close()

class PersonaSchema(BaseModel):
    cedula: str
    nombre1: str
    nombre2: str | None = None
    apellido1: str
    apellido2: str  | None = None
    fecha_nacimiento: datetime
    foto: str
class LocalidadSchema(BaseModel):
    parroquia: str
    direccion: str
    telefono: str

class RegistoSchema(BaseModel):
    perdona_id:int
    localidad_id: int
    nombre_ayuda: str
    descicion: str
    valor: float
    fecha_mregistro: datetime 

@app.get("/")
def home():
    return {"mensaje":"Bienvenido a la API del curso"}


@app.get("/personas")
def get_petsonas(db: Session = Depends(get_db)):
    return db.query(Persona).all()

@app.post("/agregar_personas")
def creat_persona(nuevaPersona: PersonaSchema, db: Session = Depends(get_db)):
    db_persona = Persona(**nuevaPersona.dict())
    db.add(db_persona)
    db.commit()
    db.refresh(db_persona)
    return db_persona
