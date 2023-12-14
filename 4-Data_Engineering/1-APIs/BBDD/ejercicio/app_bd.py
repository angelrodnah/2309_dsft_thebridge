# import json
from flask import Flask, request, jsonify
import sqlite3
import os

os.chdir(os.path.dirname(__file__))

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def welcome():
    return "Welcome to mi API conected to my books database"

# 0.Ruta para obtener todos los libros
@app.route('/v1/resources/books')
def get_all():
    connection = sqlite3.connect('books.db')
    cursor = connection.cursor()
    query = "SELECT * FROM books"
    result = cursor.execute(query).fetchall()
    connection.close()
    return jsonify(result)

# 1.Ruta para obtener el conteo de libros por autor ordenados de forma descendente
@app.route('/v1/resources/booksbyauthor')
def get_all_author():
    connection = sqlite3.connect('books.db')
    cursor = connection.cursor()
    query = '''SELECT 
                author,
                COUNT(*)
               FROM books
               GROUP BY 1
               ORDER BY 2 DESC'''
    result = cursor.execute(query).fetchall()
    connection.close()
    return jsonify(result)

# 2.Ruta para obtener los libros de un autor como argumento en la llamada
@app.route('/v1/resources/books/author')
def book_author():
    if 'author' not in request.args:
        return "Author argument missing", 400
    else:
        try:
            author = request.args['author'] # Asimov OR 1=1
            connection = sqlite3.connect('books.db')
            cursor = connection.cursor()
            query = '''SELECT 
                        *
                    FROM books
                    WHERE author LIKE ?'''
            result = cursor.execute(query, ("%" + author + "%",)).fetchall()
            connection.close()
            return jsonify(result), 200
        except Exception as e:
            return jsonify({"error":str(e)}), 500


# 3.Ruta para obtener los libros filtrados por título, publicación y autor
@app.route('/v1/resources/books/filters')
def book_filters():
    if 'author' not in request.args and 'published' not in request.args and 'title' not in request.args:
        return "Filters missing", 400
    else:
        try:
            author = request.args['author'] # Asimov OR 1=1
            published = request.args['published']
            title = request.args['title']
            connection = sqlite3.connect('books.db')
            cursor = connection.cursor()
            query = '''SELECT 
                        *
                    FROM books
                    WHERE author LIKE ?
                          AND title LIKE ?
                          AND published = ?'''
            result = cursor.execute(query, ("%" + author + "%","%" + title + "%", published)).fetchall()
            connection.close()
            return jsonify(result), 200
        except Exception as e:
            return jsonify(result), 500

app.run()