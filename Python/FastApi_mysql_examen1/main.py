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

# class Estudiante(BaseModel):
#     Id: int
#     Nombre: str
#     Apellido: str

# class Notas(BaseModel):
#     Id_estudiante: int
#     Matematicas: int
#     Ingles: int
#     Español: int

@app.get("/", response_class=HTMLResponse)
def Home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/estudiantes", response_class=HTMLResponse)
def get_estudiantes(request: Request):
    conn = mysql.connector.connect(**dbconfig)
    cursor = conn.cursor(dictionary=True)
    query = """
        SELECT 
            e.Id,
            e.Nombre,
            e.Apellido,
            n.Matematicas,
            n.Ingles,
            n.Español
        FROM estudiante e
        JOIN notas n ON n.Id = e.Id
    """
    cursor.execute(query)
    estudiantes = cursor.fetchall()
    cursor.close()
    conn.close()
    return templates.TemplateResponse("gestionEstudiantes.html", {"request": request, "estudiantes": estudiantes})

@app.get("/crearEstudiantes", response_class=HTMLResponse)
def formulario_crear_estudiante(request: Request):
    return templates.TemplateResponse("crearEstudiante.html", {"request": request})

@app.post("/crearEstudiantes", response_class=HTMLResponse)
def crear_estudiante(
    request: Request,
    Id: int = Form(...),
    Nombre: str = Form(...),
    Apellido: str = Form(...),
    Español: int = Form(...),
    Ingles: int = Form(...),
    Matematicas: int = Form(...)
):

    conn = mysql.connector.connect(**dbconfig)
    cursor = conn.cursor()
    query = "INSERT INTO estudiante (Id, Nombre, Apellido) VALUES (%s, %s, %s)"
    cursor.execute(query, (Id, Nombre, Apellido))

    query_notas = "INSERT INTO notas (Id, Matematicas, Ingles, Español) VALUES (%s, %s, %s, %s)"
    cursor.execute(query_notas, (Id, Matematicas, Ingles, Español))
    conn.commit()
    cursor.close()
    conn.close()
    return RedirectResponse(url="/estudiantes", status_code=303)

@app.get("/editarEstudiantes/{Id}", response_class=HTMLResponse)
def mostrar_formulario_actualizacion(Id: int, request: Request):
    conn = mysql.connector.connect(**dbconfig)
    cursor = conn.cursor(dictionary=True)
    
    query_notas = "SELECT * FROM notas WHERE Id = %s"
    cursor.execute(query_notas, (Id,))
    notas = cursor.fetchone() 

    cursor.execute("SELECT * FROM estudiante WHERE Id = %s", (Id,))
    estudiante = cursor.fetchone() 

    cursor.close()
    conn.close()
    
    return templates.TemplateResponse("actualizarEstudiante.html", {
        "request": request,
        "estudiante": estudiante,
        "notas": notas 
    })


@app.post("/editarEstudiantes", response_class=HTMLResponse)
def actualizar_estudiante(
    request: Request,
    Id: int = Form(...),
    Nombre: str = Form(...),
    Apellido: str = Form(...),
    Español: int = Form(...),
    Ingles: int = Form(...),
    Matematicas: int = Form(...)
    ):

    conn = mysql.connector.connect(**dbconfig)
    cursor = conn.cursor()
    query = "UPDATE estudiante SET Nombre = %s, Apellido = %s WHERE Id = %s"
    query_notas = "UPDATE notas SET Matematicas = %s, Ingles = %s, Español = %s WHERE Id = %s"
    cursor.execute(query_notas, (Matematicas, Ingles, Español, Id))
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


