from flask import Flask, request, render_template
import pickle
import pandas as pd

import numpy as np
app = Flask(__name__)

model = pickle.load(open("model.pkl","rb"))




@app.route('/',methods=['GET'])
def home():
    return render_template('index.html')



@app.route('/predict',methods = ['POST'])
def predict():
    if request.method == 'POST':
        myDict = request.form
        Incident_Radiation = int(myDict['Incident_Radiation'])
        Inlet_Water_Temperature	 = int(myDict['Inlet_Water_Temperature'])
        Temperature = int(myDict['Temperature(LCZ)'])
        Ambient_Temperature = int(myDict['Ambient_Temperature'])
        prediction=model.predict([[Incident_Radiation,Inlet_Water_Temperature,Temperature,Ambient_Temperature]])
        output = round(prediction[0],2)
        return render_template('show.html',prediction_text=output)


if __name__ == "__main__":
    app.run(debug=True)