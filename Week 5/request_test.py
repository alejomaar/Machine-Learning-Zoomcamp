import requests

url = 'http://localhost:9696/predict'

customer ={"reports": 0, "share": 0.001694, "expenditure": 0.12, "owner": "yes"}
customer_id = 'xyz-123'

response = requests.post(url, json=customer).json()

print(response)

if response['is_credit'] == True:
    print('Customer %s will get a credit' % customer_id)
else:
    print('Customer %s will not get a credit' % customer_id)