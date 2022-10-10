import pickle

from flask import Flask
from flask import request
from flask import jsonify

model_file = 'model1.bin'
dv_file = 'dv.bin'

with open(model_file,'rb') as f:
    model = pickle.load(f)
    
with open(dv_file,'rb') as f:
    dv = pickle.load(f)

app = Flask('credit')

@app.route('/predict', methods=['POST'])
def predict():
    customer = request.get_json()

    X = dv.transform([customer])
    #Customers can have a credit card `(1)` or not `(0)`.
    #The order of the prediction has the form:
    #[`Probability of not getting a credit card`, `Probability of getting a credit card`]
    
    y_pred = model.predict_proba(X)[0, 1]
    is_credit = y_pred >= 0.5

    result = {
        'credit_probability': float(y_pred),
        'is_credit': bool(is_credit)
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)
