from db_config import db
from models import Persona

resultado = db.query(Persona).first()

print(resultado.nombre1)