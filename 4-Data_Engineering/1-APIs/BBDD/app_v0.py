from flask import Flask, jsonify, request
from datos_dummy import books

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>My first API</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

# 1.Ruta para obtener todos los libros
@app.route('/v0/books', methods=['GET'])
def all_books():
    return jsonify(books)
    
# 2.Ruta para obtener un libro concreto mediante su id como parámetro en la llamada
# @app.route('/v0/book_id', methods=['GET'])




# 3.Ruta para obtener un libro concreto mediante su título como parámetro en la llamada de otra forma
# @app.route('/v0/book/<string:title>', methods=["GET"])


# 4.Ruta para obtener un libro concreto mediante su titulo dentro del cuerpo de la llamada  
# @app.route('/v1/book', methods=["GET"])
    

# 5.Ruta para añadir un libro mediante un json en la llamada



# 6.Ruta para añadir un libro mediante parámetros
 

# 7.Ruta para modificar un libro


# 8.Ruta para eliminar un libro


app.run()