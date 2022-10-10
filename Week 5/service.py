import pickle

from flask import Flask
from flask import request
from flask import jsonify


def get_model(model_file,dv_file):
    with open(model_file,'rb') as f:
        model = pickle.load(f)    
    with open(dv_file,'rb') as f:
        dv = pickle.load(f)
    return model,dv

app = Flask('credit')

#Customers can have a credit card `(1)` or not `(0)`.
#The order of the prediction has the form:
#[`Probability of not getting a credit card`, `Probability of getting a credit card`]

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    client = data['client']
    model = data['model']
    
    model,dv = get_model(model,'dv.bin')    

    X = dv.transform([client])
    
    y_pred = model.predict_proba(X)[0, 1]
    is_credit = y_pred >= 0.5

    result = {
        'credit_probability': float(y_pred),
        'is_credit': bool(is_credit)
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)
