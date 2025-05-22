from fastapi import FastAPI, HTTPException
from pydantic import BaseModel 
import mysql.connector

app = FastAPI()

db_config = {
    "host": "localhost",
    "database": "fastapi_db",
    "user": "root",
    "password": "root"
}

@app.get("/")
def read_root():
    return {"Mensaje": "Hola mundo"}

@app.get("/saludo/{nombre}")
def saludar(nombre: str):
    return {"mensaje": f"Hola {nombre}"}

# Modelo Pydantic
class Persona(BaseModel):
    Id: int
    nombre: str
    edad: int
    peso: float
    altura: float

@app.get("/personas")
def listar_personas():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("SELECT Id, nombre, edad, peso, altura FROM usuario")
    resultados = cursor.fetchall()
    cursor.close()
    conn.close()
    return [{"Id": row[0], "nombre": row[1], "edad": row[2], "peso": row[3], "altura": row[4]} for row in resultados]

@app.post("/personas")
def crear_persona(persona: Persona):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    sql = "INSERT INTO usuario (Id, nombre, edad, peso, altura) VALUES (%s, %s, %s, %s, %s)"
    valores = (persona.Id, persona.nombre, persona.edad, persona.peso, persona.altura)
    cursor.execute(sql, valores)
    conn.commit()
    cursor.close()
    conn.close()
    return {"mensaje": "Persona creada correctamente"}

@app.put("/personas")
def editar_usuario(persona: Persona):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    sql = "UPDATE usuario SET nombre = %s, edad = %s, peso = %s, altura = %s WHERE Id = %s"
    valores = (persona.nombre, persona.edad, persona.peso, persona.altura, persona.Id)
    cursor.execute(sql, valores)
    conn.commit()
    cursor.close()
    conn.close()
    return {"mensaje": "Persona actualizada correctamente"}

@app.delete("/personas/{Id}")
def eliminar_persona(Id: int):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuario WHERE Id = %s", (Id,))
    persona = cursor.fetchone()
    if not persona:
        cursor.close()
        conn.close()
        raise HTTPException(status_code=404, detail="Persona no encontrada")

    cursor.execute("DELETE FROM usuario WHERE Id = %s", (Id,))
    conn.commit()
    cursor.close()
    conn.close()
    return {"mensaje": f"Persona con ID {Id} eliminada correctamente"}



  

# @app.get("/personas/{Id}")
# def crear_personas(persona: persona):
#     return {"Mensaje": f"Bienvenido señor: {persona.nombre}, {persona.edad}, {persona.peso}, {persona.altura}"}

# @app.post("/personas")
# def crear_personas(persona: persona):
#     return {"Mensaje": f"Bienvenido señor: {persona.Id}, {persona.nombre}, {persona.edad}, {persona.peso}, {persona.altura}"}

# @app.put("/personas/{Id}")
# def crear_personas(persona: persona):
#     return {"Mensaje": f"Actualiza persona:{persona.Id},{persona.nombre}, {persona.edad}, {persona.peso}, {persona.altura}"}

# @app.delete("/personas/{Id}")
# def crear_personas(persona: persona):
#     return {"Mensaje": f"ELIMINADO:{persona.Id}"}
#para ejecutarlo 'uvicorn main:app --reload'"""