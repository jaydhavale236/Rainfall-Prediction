from calendar import month
from tkinter import Variable
from unittest import result
from flask import Flask, render_template, request, jsonify
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
import pickle
import os

app = Flask(__name__)
model = pickle.load(open('rainfall.pkl', 'rb'))

    
@app.route("/")
def index():
    return render_template("new.html")

@app.route("/predict", methods = ['POST'])
def predict():
    try:
        day = int(request.form["day"])
        pressure = float(request.form["pressure"])
        maxtemp = float(request.form["maxtemp"])
        temparature = float(request.form["temparature"])
        mintemp = float(request.form["mintemp"])
        dewpoint = float(request.form["dewpoint"])
        humidity = int(request.form["humidity"])
        cloud = int(request.form["cloud"])
        sunshine = float(request.form["sunshine"])
        winddirection = int(request.form["winddirection"])
        windspeed = float(request.form["windspeed"])

        # Predict using the loaded model
        prediction = model.predict([[day, pressure, maxtemp, temparature, mintemp, dewpoint, humidity, cloud, sunshine, winddirection, windspeed]])


        return render_template("new.html", prediction_text='{}'.format(prediction))
    except Exception as e:
        return jsonify({prediction: str(e)})
if __name__ == '__main__':
    app.run(debug=True)
