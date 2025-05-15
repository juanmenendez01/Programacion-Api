from flask import Flask, request, render_template, redirect, url_for

import mysql.connector # pip install mysql-connector-python

app = Flask(__name__)

#configuracion de la conexion

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'flask_db'
}

@app.route('/')
def index():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Personas")
    personas = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template('index.html', personas=personas)


@app.route('/agregar', methods=['GET', 'POST'])
def agregar():
    if request.method == 'POST':
        nombre = request.form['nombre']
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Personas (nombre) VALUES (%s)", (nombre,))
        conn.commit()
        cursor.close()
        conn.close()
        # Redirigir a la página principal después de agregar    
        return redirect(url_for('index'))
    # Si es un GET, simplemente mostrar el formulario
    return render_template('agregar.html')

if __name__ == '__main__':
    app.run(debug=True)