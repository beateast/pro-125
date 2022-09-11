from crypt import methods
from flask import flask, jsonify, request
from classifier import get_prediction
from distutils import debug
from crypt import methods
    

app = Flask(__name__)
@app.route("/predict_alphbet", methods["post"])
def predict_data():
    image = request.files.get("alphabet")
    prediction = get_prediction(image)
    return jsonify({
        "prediction":prediction
    })
    if __name__ == "__main__":
        app.run(debug = True)