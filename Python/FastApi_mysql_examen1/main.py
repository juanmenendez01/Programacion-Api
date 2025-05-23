from fastapi import Request, Form
from fastapi.responses import RedirectResponse
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import mysql.connector
from fastapi import HTTPException
import os

app = FastAPI()

templates = Jinja2Templates(directory=os.path.join(os.path.dirname(__file__), "templates"))

# Database connection
dbconfig = {
    'host': 'localhost',
    'database': 'estudiantes',
    'user': 'root',
    'password': 'root',
}


@app.get("/", response_class=HTMLResponse)
def Home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

class Estudiante(BaseModel):
    Id: int
    Nombre: str
    Apellido: str

@app.get("/estudiantes", response_class=HTMLResponse)
def get_estudiantes(request: Request):
    conn = mysql.connector.connect(**dbconfig)
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM estudiante"
    cursor.execute(query)
    estudiantes = cursor.fetchall()
    cursor.close()
    conn.close()
    return templates.TemplateResponse("gestionEstudiantes.html", {"request": request, "estudiantes": estudiantes})


@app.get("/estudiantes/{id}")
def estudiante_id(id: int):
    conn = mysql.connector.connect(**dbconfig)
    cursor = conn.cursor()
    query = "SELECT * FROM estudiante WHERE id = %s"
    cursor.execute(query, (id,))
    estudiante = cursor.fetchone()
    cursor.close()
    conn.close()
    if estudiante:
        return {"Id" : estudiante[0], "Nombre": estudiante[1], "Apellido": estudiante[2]}
    else:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")
    
@app.get("/crearEstudiantes", response_class=HTMLResponse)
def formulario_crear_estudiante(request: Request):
    return templates.TemplateResponse("crearEstudiante.html", {"request": request})

@app.post("/crearEstudiantes", response_class=HTMLResponse)
def crear_estudiante(request: Request,
    Id: int = Form(...),
    Nombre: str = Form(...),
    Apellido: str = Form(...)):
    
    estudiante = Estudiante(Id=Id, Nombre=Nombre, Apellido=Apellido)

    conn = mysql.connector.connect(**dbconfig)
    cursor = conn.cursor()
    query = "INSERT INTO estudiante (Id, Nombre, Apellido) VALUES (%s, %s, %s)"
    cursor.execute(query, (estudiante.Id, estudiante.Nombre, estudiante.Apellido))
    conn.commit()
    cursor.close()
    conn.close()
    return RedirectResponse(url="/estudiantes", status_code=303)

@app.get("/editarEstudiantes/{Id}", response_class=HTMLResponse)
def mostrar_formulario_actualizacion(Id: int, request: Request):
    conn = mysql.connector.connect(**dbconfig)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM estudiante WHERE Id = %s", (Id,))
    estudiante = cursor.fetchone()
    cursor.close()
    conn.close()
    return templates.TemplateResponse("actualizarEstudiante.html", {
        "request": request,
        "estudiante": estudiante
    })

@app.post("/editarEstudiantes", response_class=HTMLResponse)
def actualizar_estudiante(
    request: Request,
    Id: int = Form(...),
    Nombre: str = Form(...),
    Apellido: str = Form(...)
    ):

    conn = mysql.connector.connect(**dbconfig)
    cursor = conn.cursor()
    query = "UPDATE estudiante SET Nombre = %s, Apellido = %s WHERE Id = %s"
    cursor.execute(query, (Nombre, Apellido, Id))
    conn.commit()
    cursor.close()
    conn.close()
    return RedirectResponse(url="/estudiantes", status_code=303)

@app.post("/eliminarEstudiantes", response_class=HTMLResponse)
def eliminar_estudiante(request: Request,
                        Id: int = Form(...)):
    conn = mysql.connector.connect(**dbconfig)
    cursor = conn.cursor()

    query_notas = "DELETE FROM notas WHERE Id = %s"
    cursor.execute(query_notas, (Id,))

    query = "DELETE FROM estudiante WHERE Id = %s"
    cursor.execute(query, (Id,))
    conn.commit()
    cursor.close()
    conn.close()
    return RedirectResponse(url="/estudiantes", status_code=303)


class Notas(BaseModel):
    Id: int
    Id_Estudiante: int
    Matematicas: float
    Ingles: float
    Español: float

@app.post("/Notas")
def crear_notas(notas: Notas):
    conn = mysql.connector.connect(**dbconfig)
    cursor = conn.cursor()
    query = "SELECT e.Id, e.Nombre, e.Apellido, n.Matematicas, n.Ingles, n.Español FROM estudiante e JOIN notas n ON e.Id = n.Id_Estudiante WHERE e.Id = %s"
    cursor.execute(query, (notas.Id, notas.Id_Estudiante, notas.Matematicas, notas.Ingles, notas.Español))
    conn.commit()
    cursor.close()
    conn.close()
    return {"mensaje": "Notas creadas correctamente", "notas": notas}

@app.get("/estudiantesNotas/{id}")
def estudiante_notas(id: int):
    conn = mysql.connector.connect(**dbconfig)
    cursor = conn.cursor()
    query = "SELECT e.Id, e.Nombre, e.Apellido, n.Matematicas, n.Ingles, n.Español FROM estudiante e JOIN notas n ON e.Id = n.Id WHERE e.Id = %s"
    cursor.execute(query, (id,))
    estudiante = cursor.fetchall()
    cursor.close()
    conn.close()
    if estudiante:
        return [{"Id" : e[0], "Nombre": e[1], "Apellido": e[2], "Matematicas": e[3], "Ingles": e[4], "Español": e[5]} for e in estudiante]
    else:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")
    



