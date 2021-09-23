from balance import app
from flask import render_template
from balance.utilities import fecha_actual
from datetime import date, datetime

@app.route('/')
def inicio():
    now = datetime.now()
    return render_template('inicio.html', fecha_hoy = fecha_actual(now))

@app.route('/nuevo', methods=['GET', 'POST'])
def nuevo():
    return 'Página de alta de movimientos'

@app.route('/borrar/<int:id>', methods=['GET', 'POST'])
def borrar(id):
    return f'Páginade borrado {id}'