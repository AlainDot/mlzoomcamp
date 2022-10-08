# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 17:18:28 2022
"""


import pickle
import numpy as npy

from flask import Flask, request, jsonify

def predict_single(customer, dv, model):
    X = dv.transform([customer])
    y_pred = model.predict_proba(X)[:, 1]
    return y_pred[0]


#with open('churn-model.bin', 'rb') as f_in:
#    dv, model = pickle.load(f_in)

# re-Load dicVectorizer
filDvt = 'dv.bin'
with open(filDvt, 'rb') as fil: 
    dvt = pickle.load(fil)
print(' > DicVertorizer loaded from file!')


# re-Load Model
filMod = 'model2.bin'
with open(filMod, 'rb') as fil: 
    modLor = pickle.load(fil)
print(' > Model loaded from file!')


app = Flask('card')


@app.route('/predict', methods=['POST'])
def predict():
    print('     > predict function Beg'   )
    customer = request.get_json()

    prediction = predict_single(customer, dvt, modLor)
    card = prediction >= 0.5
    
    result = {
        'card_probability': float(prediction),
        'card': bool(card),
    }

    print('     > predict function End'   )
    return jsonify(result)


if __name__ == '__main__':
    print(' > __main__ starting app.run')
    app.run(debug=True, host='0.0.0.0', port=9696)