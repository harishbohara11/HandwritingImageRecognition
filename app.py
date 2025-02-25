from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np

app = Flask(__name__)

# Load the best saved models
model1 = tf.keras.models.load_model('model1_best.h5')
model2 = tf.keras.models.load_model('model2_best.h5')

def ensemble_predictions(data):
    pred1 = model1.predict(data)
    pred2 = model2.predict(data)
    return (pred1 + pred2) / 2.0

@app.route('/hello', methods=['GET'])
def hello():
    return "Hello world!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    images = np.array(data.get("images"))
    
    # Normalize images as done during training
    images = images.astype("float32") / 255.0
    if len(images.shape) == 3:
        images = images.reshape(-1, 28, 28, 1)
    
    ensemble_pred = ensemble_predictions(images)
    predictions = np.argmax(ensemble_pred, axis=1)
    return jsonify({'predictions': predictions.tolist()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
