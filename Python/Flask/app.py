from flask import Flask, render_template
from modules import reportes, aire, censo, educacion, movilidad

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/reportes')
def modulo_reportes():
    return reportes.mostrar_reportes()

@app.route('/aire')
def modulo_aire():
    return aire.mostrar_aire()

@app.route('/censo')
def modulo_censo():
    return censo.mostrar_censo()

@app.route('/educacion')
def modulo_educacion():
    return educacion.mostrar_educacion()

@app.route('/movilidad')
def modulo_movilidad():
    return movilidad.mostrar_movilidad()


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8080)
