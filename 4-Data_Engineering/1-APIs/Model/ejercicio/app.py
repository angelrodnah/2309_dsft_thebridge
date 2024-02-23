from flask import Flask, request, render_template
import sqlite3
import pickle
import pandas as pd

app = Flask(__name__)

with open('data/new_advertising_model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ingest', methods=['POST'])
def ingest():
    data = request.get_json()
    new_data = data.get('data', None)
    if not new_data:
        return {"error":"No se proporcionaron datso para agregar a la bbdd"}, 400

    try:
        connection = sqlite3.connect('data/advertising.db')
        cursor = connection.cursor()
        query = "INSERT INTO campañas VALUES (?,?,?,?)"
        for valor in new_data:
            cursor.execute(query, valor)
        connection.commit()
        connection.close()
        return {'message': 'Datos ingresados correctamente'}, 200
    except Exception as e:
        return {'error':str(e)}, 500
    
@app.route('/predict', methods=['GET'])
def predict():
    data = request.get_json()
    input_data = data.get('data', None)
    if not input_data:
        return {"error":"No se proporcionaron los datos necesarios para realizar la predicción. Ej:{'data': [[100, 100, 200]]}"}, 400
    try:
        predictions = []
        for valor in input_data:
            predictions.append(round(model.predict([valor])[0],2))
        return {"prediction":predictions}, 200
    except Exception as e:
        return {'error':str(e)}, 500
    
@app.route('/retrain', methods=['POST'])
def retrain():
    try:
        connection = sqlite3.connect('data/advertising.db')
        cursor = connection.cursor()
        query = '''SELECT * FROM campañas'''
        result = cursor.execute(query).fetchall()
        df = pd.DataFrame(result)
        model.fit(df.iloc[:,:-1], df.iloc[:,-1])
        with open('data/new_advertising_model.pkl', 'wb') as file:
            pickle.dump(model, file)
        return {'message': 'Modelo reentrenado correctamente.'}, 200
    except Exception as e:
        return {'error':str(e)}, 500

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')