from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World with FastAPI!"}

@app.get("/saludo/{nombre}")
async def saludo(nombre: str):
    return {"message": f"Hola {nombre}!"}

class Persona(BaseModel):
    id: int
    nombre: str
    edad: int

@app.post("/persona")
async def crearPersona(persona: Persona):
    return {"message": f"Persona creada: {persona.nombre}, Edad: {persona.edad}"}
    
@app.delete("/persona/{id_person}")
async def eliminarPersona(persona: Persona):
    return {"message": f"Persona eliminada: {persona.nombre}"}

@app.put("/persona/{id_person}")
async def actualizarPersona(persona: Persona):
    return {"message": f"Persona actualizada: {persona.nombre}, Edad: {persona.edad}"}

@app.delete("/persona/{id_person}")
async def eliminarPersona(id_person: int):
    return {"message": f"Persona eliminada con ID: {id_person}"}