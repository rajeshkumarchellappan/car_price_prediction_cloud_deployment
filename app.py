from flask import Flask, request, render_template
from flask_cors import cross_origin
import jsonify
import sklearn
import requests
import numpy as np
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))


@app.route('/',methods=['GET'])
#@cross_origin()
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
#@cross_origin()
def predict():
    Fuel_Type_Diesel = 0
    if request.method == "POST":
        # input variables
        Year = int(request.form['Year'])
        Year = 2021-Year
        Present_Price = float(request.form['Present_Price'])
        Kms_Driven = int(request.form['Kms_Driven'])
        Owner = int(request.form['Owner'])
        Fuel_Type_Petrol= request.form['Fuel_Type_Petrol']
        if (Fuel_Type_Petrol == 'Petrol'):
            Fuel_Type_Petrol = 1
            Fuel_Type_Diesel = 0
        elif(Fuel_Type_Petrol == 'Diesel') :
            Fuel_Type_Petrol = 0
            Fuel_Type_Diesel = 1

        else:
            Fuel_Type_Petrol = 0
            Fuel_Type_Diesel = 0


        Seller_Type_Individual = request.form['Seller_Type_Individual']
        if (Seller_Type_Individual == 'Individual'):
            Seller_Type_Individual = 1
            #Seller_Type_Dealer = 0
        else:
            Seller_Type_Individual = 0
            #Seller_Type_Dealer = 1
        Transmission_Manual = request.form['Transmission_Manual']
        if (Transmission_Manual == 'Manual'):
            Transmission_Manual = 1
            # Transmission_Automatic = 0
        else:
            Transmission_Manual = 0
            # Transmission_Automatic = 1

        prediction = model.predict([[Year, Present_Price, Kms_Driven, Owner, Fuel_Type_Diesel,
                                     Fuel_Type_Petrol, Seller_Type_Individual, Transmission_Manual]])
        output = round(prediction[0], 2)

        return render_template('index.html', prediction_text = 'The predicted selling price for the car is {}'.format(output))
    else:

        return render_template('index.html')


if __name__ == "__main__":
   app.run(debug=True)