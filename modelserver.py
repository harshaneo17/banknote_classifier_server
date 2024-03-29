import pandas as pd
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

# Create flask app
app = Flask(__name__)
model = pickle.load(open("banknotesmodel.pkl", "rb"))

@app.route("/")
def Home():
    return render_template("index.html")

@app.route("/predict", methods = ["POST"])

#For web application
def predict():
    float_features = [float(x) for x in request.form.values()]
    features = [np.array(float_features)]
    prediction = model.predict(features)
    return render_template("index.html", prediction_text = f"The bank note is {prediction}")
    
""" The below method preferable than the render_template method.
    Instead of rendering an html templte, return the json and then
    use javascript to write the data to the html on the page.
    All it would need is an ajax call to get the prediction from the server.
    This opens up the model server and means it can be consumed by anything that
    can post and receive json."""

#For POSTMAN TESTING API
# def predict():
    # json_ = request.json
    # query_df = pd.DataFrame(json_)
    # prediction = model.predict(query_df)
    # return jsonify({"Prediction": prediction.tolist()})

if __name__ == "__main__":
    app.run(debug=True)