from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey, Float
from sqlalchemy.orm import relationship
from db_config import Base

class Persona(Base):
    __tablename__ = "persona"

    id = Column(Integer, primary_key=True, autoincrement=True)
    cedula = Column(String(10), nullable=False)
    nombre1 = Column(String(30), nullable=False)
    nombre2 = Column(String(30), nullable=True)
    apellido1 = Column(String(30), nullable=False)
    apellido2 = Column(String(30), nullable=True)
    fecha_nacimiento = Column(DateTime, nullable=False)
    foto = Column(Text, nullable=False)

class Localidad(Base):
    __tablename__ = "localidad"

    id= Column(Integer, primary_key=True,autoincrement = True)
    parroquia = Column(String(250),nullable=False)
    direccion = Column(String(250),nullable=False)
    telefono = Column(String(10),nullable=False)

class Registro(Base):
    __tablename__ = "registro"

    id= Column(Integer, primary_key=True,autoincrement = True)
    persona_id = Column(Integer,ForeignKey("persona.id"),nullable=False)
    localidad_id = Column(Integer,ForeignKey("localidad.id"),nullable=False)
    nombre_ayuda = Column(String(100),nullable=False)
    descripcion = Column(String(250),nullable=False)
    valor = Column(Float,nullable=False)
    fecha_registro = Column(DateTime,nullable=False)

    persona = relationship("Persona")
    localidad = relationship("Localidad")

class AdminAyuda(Base):
    __tablename__ = "admin_ayuda"

    nombre_usuario= Column(String(15), primary_key=True)
    clave= Column(Text,nullable=False)

class RegistroLogin(Base):
    __tablename__ = "registro_login"

    id= Column(Integer, primary_key=True,autoincrement = True)
    admin_ayuda= Column(String(15),ForeignKey("admin_ayuda.nombre_usuario"),nullable=False)
    fecha_hora= Column(DateTime,nullable=False)
    clave= Column(Text,nullable=False)

    admin = relationship("AdminAyuda")