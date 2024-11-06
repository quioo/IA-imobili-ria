from flask import Flask, request, jsonify
from flask_cors import CORS
import tensorflow as tf
import numpy as np
import joblib

app = Flask(__name__)
CORS(app)

# Carregar o modelo e o escalador
model = tf.keras.models.load_model("modelo_regressao_imoveis.h5")
scaler = joblib.load('scaler.joblib')

# Rota para previsão usando POST e JSON
@app.route("/predict", methods=["POST"])
def predict():
    # Obter os dados JSON da requisição
    data = request.get_json()

    # Extrair e converter os valores dos dados JSON
    m = data.get("m²", 0)
    qtdQuartos = data.get("qnt Quartos", 0)
    qtdBanheiro = data.get("qnt Banheiros", 0)
    idade = data.get("Idade", 0)
    garagem = data.get("Garagem", 0)
    dist = data.get("Distância centro", 0)

    # Organizar os dados em um array para o modelo
    features = np.array([[m, qtdQuartos, qtdBanheiro, idade, garagem, dist]])
    features_scaled = scaler.transform(features)
    
    # Fazer a previsão
    prediction = model.predict(features_scaled)
    preco = float(prediction[0][0])

    # Retornar o resultado como JSON
    return jsonify({"preço_previsto": preco})

if __name__ == '__main__':
    app.run(debug=True)
