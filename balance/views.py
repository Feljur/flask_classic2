from balance import app

@app.route('/')
def inicio():
    return 'Página de inicio'

@app.route('/nuevo', methods=['GET', 'POST'])
def nuevo():
    return 'Página de alta de movimientos'

@app.route('/borrar/<int:id>', methods=['GET', 'POST'])
def borrar(id):
    return f'Páginade borrado {id}'