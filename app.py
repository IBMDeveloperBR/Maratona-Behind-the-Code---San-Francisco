from flask import Flask, render_template, request, json, jsonify
import os
import json
import numpy as np
import io
from PIL import Image

app = Flask(__name__)
app.config.from_object(__name__)
port = int(os.getenv('PORT', 8080))

@app.route("/", methods=['GET'])
def hello():
    error=None
    return render_template('index.html', error=error)

@app.route("/iot", methods=['GET'])
def result():
    print(request)
    
    # Implemente sua lógica aqui e insira as respostas na variável 'resposta'
    
    resposta = {
        "iotData": "data",
        "itu": "data",
        "volumeAgua": "data",
        "fahrenheit": "data"
    }
    response = app.response_class(
        response=json.dumps(resposta),
        status=200,
        mimetype='application/json'
    )
    return response

def prepare_image(image):
    image = image.resize(size=(96,96))
    image = np.array(image, dtype="float") / 255.0
    image = np.expand_dims(image,axis=0)
    image = image.tolist()
    return image

@app.route('/predict', methods=['POST'])
def predict():
    print(request)
    image = request.files["image"].read()
    image = Image.open(io.BytesIO(image))
    image = prepare_image(image)

    # Faça uma requisição para o serviço Watson Machine Learning aqui e retorne a classe detectada na variável 'resposta'
    
    resposta = {
        "class": "data"
    }
    return resposta

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)