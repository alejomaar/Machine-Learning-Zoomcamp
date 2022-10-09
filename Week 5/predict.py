import pickle

model_file = 'model1.bin'
dv_file = 'dv.bin'

with open(model_file,'rb') as f:
    model = pickle.load(f)
    
with open(dv_file,'rb') as f:
    dv = pickle.load(f)

client = {"reports": 0, "share": 0.001694, "expenditure": 0.12, "owner": "yes"}

X = dv.transform([client])
y = model.predict_proba(X)

print(y)
print(model.classes_)
