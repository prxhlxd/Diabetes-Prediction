from flask import Flask, jsonify, request, render_template
import numpy as np
import model

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    prediction = model.process(data)
    return jsonify({'diabetes_type': int(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True)