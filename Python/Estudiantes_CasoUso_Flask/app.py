from flask import Flask, render_template, request, redirect, url_for

import mysql.connector

app = Flask(__name__)

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'Estudiantes'
}


# TODO -> QUITAR LOS ESTATICOS 
listaEstudiantes = []

listaNotas = []

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/estudiantes')
def estudiantes():
    # Conexión a la base de datos
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    query = "SELECT * FROM Estudiante"
    cursor.execute(query)
    estudiantes = cursor.fetchall()
    cursor.close()
    conn.close()
    
    return render_template("estudiantes.html", data = estudiantes)

@app.route('/registrar')
def registrar():
    return render_template("registrar.html")

@app.route("/registrar", methods=['POST'])
def enviar_datos():
   
    if request.method == 'POST':
        id = request.form['Id']
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        matematicas = request.form['mate']
        ingles = request.form['ingles']
        espa = request.form['espa']

        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        query = "Insert into Estudiante (Id, Nombre, Apellido) values (%s, %s, %s)"
        values = (id, nombre, apellido)
        query2 = "Insert into Notas (Id, Matematicas, Español, Ingles) values (%s, %s, %s, %s)"
        values2 = (id, matematicas, espa, ingles)
        cursor.execute(query, values)
        cursor.execute(query2, values2)
        conn.commit()
        cursor.close()
        conn.close()
  
  # TODO -> Guardar esta información en los arreglos

    return redirect(url_for('estudiantes'))

@app.route('/Notas')
def Notas():
    # Conexión a la base de datos
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    query = "SELECT * FROM Estudiante"
    cursor.execute(query)
    estudiantes = cursor.fetchall()
    cursor.close()
    conn.close()
    
    return render_template("notasEstudiante.html", consulta = estudiantes)


# Hay que completar la funcionalidad de esto, para hacer que filter por nombre de estudiante y ya 

@app.route('/Notas', methods=['POST'])
def Filtar():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    if request.method == 'POST':
        estudiante_id = request.form['filtro']

        print("ID ESTUDIANTE: ", estudiante_id)

        queryEstudiantes = "SELECT * FROM Estudiante"
        cursor.execute(queryEstudiantes)
        estudiantes = cursor.fetchall()

        query = f"SELECT * FROM Estudiante AS e INNER JOIN Notas AS n ON e.Id = n.Id WHERE e.Id = %s"
        cursor.execute(query, (estudiante_id,))
        notas = cursor.fetchall()

        cursor.close()
        conn.close()

        promedio = promedio = sum(int(fila[4]) for fila in notas) / len(notas) if notas else 0
        

        return render_template("notasEstudiante.html", consulta=notas, estu=estudiantes, promedio = promedio)


    return render_template("notasEstudiante.html", consulta = estudiantes)
    

if __name__ == '__main__':
    app.run(debug=True)