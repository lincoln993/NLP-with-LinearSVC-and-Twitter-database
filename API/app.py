from flask import Flask, json, jsonify, request
from joblib import load

app = Flask(__name__)

@app.route("/")
def index():
    if 'query' not in request.args:
        return jsonify({"prediction": None, "Message": "Send me a text"})

    query = request.args.get("query")
    model = load("model.joblib")
    labels = ['Negativo', 'Positivo']

    predict = model.predict([query])
    predicition = labels[predict[0]]

    return jsonify({"prediction": predicition})