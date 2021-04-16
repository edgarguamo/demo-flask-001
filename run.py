"""
Introducción a Flask
https://parzibyte.me/blog
"""
from flask import Flask

app = Flask(__name__)


@app.route('/')
def inicio():
    return "<h1>Hola mundo con Flask</h1>"

@app.route('/suma')
def suma():
    resultado = 10 + 10
    return "<h3>10 + 10 = %d</h3>" % (resultado)

@app.route('/listado')
def listado():
    return """
            <h1>Listado de la Compra:</h1>
            <p>- Arroz (25 lb)<br/>
            - Queso (3 lb)<br/>
            - Carne de Res (2 kg)<br/>
            - Sal (1/2 kg)<br/>
            - Pimienta (1/5 kg)<br/>
            - Pescado (8 unidades)</p>
           """
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
