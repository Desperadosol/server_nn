from flask import Flask, request
from flask_cors import CORS
import tensorflow as tf
import numpy as np
import json

from checklist import generateSample
from configurateModel import create_model

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return "Hello World"

@app.route('/api/prediction', methods=['POST'])
def prediction():
    model = create_model(18, 64, 64, 32, 16)
    model.load_weights('./model.keras')
    inputs = request.get_json()['answers']
    prediction = model.predict(np.array([inputs]))[0]
    print(prediction)
    
    subjects = request.get_json()['subjects']
    for i in range(len(prediction)):
        subjects[i]['score'] = round(float(prediction[i]*100), 2)
    print(subjects)
          
    return {'recommendations': [float(i) for i in prediction],
            'subjects': subjects}


@app.route('/api/train', methods = ['POST'])
def train_model():
    model = create_model(18, 64, 64, 32, 16)
    model.load_weights('./model.keras')
    inputs = request.get_json()['answers']
    targets = request.get_json()['targets']
    try:
        model.fit(np.array([inputs]), np.array([targets]), epochs=5)
        model.save('./model.keras')
        result = "Model trained"
    except Exception as e:
        result = "Error: " + str(e)
    return { "result":  result}


@app.route('/api/sample', methods = ['POST'])
def get_sample():
    subjects = request.get_json()['subjects']
    return { "sample": generateSample(subjects)}

if __name__ == "__main__":
    # app.run(debug=True, port=os.getenv("PORT", default=5000))
    app.run()