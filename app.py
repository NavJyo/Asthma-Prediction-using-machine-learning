# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 22:38:33 2021

@author: Ananya M Menon
"""


from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('Asthma.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('Asthma.html')


@app.route('/predict', methods = ['GET', 'POST'])
def predict():

    int_features = [ int (x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = int (prediction[0])
    print (output)
    
    if output == 0:
        return render_template('Asthma.html', prediction_text= 'Yipeeeee ! You shall not suffer from Asthma :)')
    else:
        return render_template('Asthma.html', prediction_text= 'Ouch! You might suffer from Asthma :(')


if __name__ == "__main__":
    app.run(debug=True)
    
