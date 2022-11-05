import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import GridSearchCV
import bentoml

# READ THIS BEFORE RUNNING THE SCRIPT
'''
Many steps were taken and various models explored to arrive at the final model.
This script only contains the final part of the process, check the 'notebook.ipynb'
file for the full context
'''
# 1) Get and clean the data

target = 'gender'
features = [
 'height',
 'weight',
 'life_struggles',
 'pc',
 'shopping',
 'war',
 'action',
 'cars',
 'science_and_technology',
 'romantic',
 'reading',
 'western',
 'dancing',
 'theatre',
 'darkness',
 'gender']


df = pd.read_csv('responses.csv')

df.columns = df.columns.str.lower().str.replace(' ','_').str.replace('-','')

#Delete rows that have no target variable
df =df.dropna(subset=[target])

df = df[features]

#Convert target variable (male or female) into binary
df['gender'] = (df['gender']=='male').astype('int')

# 2) Train/Test (Cross validation in 5 step)

df_train, df_test = train_test_split(df, test_size=0.2, random_state=1)

y_train = df_train.gender.values
y_test = df_test.gender.values

del df_train['gender']
del df_test['gender']

# 3) Replace null based on test dataset
categorical = list(df_train.dtypes[df.dtypes == 'object'].index)
numerical = list(df_train.dtypes[df.dtypes != 'object'].index)

def prepare_X(actual_df):
    df_prepare = actual_df.copy()
    # Replace nulls categorical values with mode
    for column in categorical:
        df_prepare[column].fillna(df_train[column].mode()[0], inplace=True)
    # Replace null numerical values with mean
    df_prepare[numerical] = df_prepare[numerical].fillna(df_train.mean())
    return df_prepare


prepare_train = prepare_X(df_train)
prepare_test = prepare_X(df_test)

# 4) Apply one hot 
dv = DictVectorizer(sparse=False)

train_dicts = prepare_train.to_dict(orient='records')
test_dicts = prepare_test.to_dict(orient='records')

X_train = dv.fit_transform(train_dicts)
X_test = dv.transform(test_dicts)

# 5) Train & tunning model

model = RandomForestClassifier(random_state=1, n_jobs=-1,warm_start=True) #Fixed Hyperarameters here

tunning = {'n_estimators':list(range(10, 201, 10)),'max_depth':[10, 15, 20, 25]} #Hyperarameters to tune

# Explanation
# -- For each combination of parameters in `tunning`, 5 cross validations will be performed. 
classifier = GridSearchCV(model,tunning,cv=5,return_train_score=False,n_jobs=-1,verbose=3)
classifier.fit(X_train,y_train)
# -- Return the best model in all cross validations :)  
rf_classifier = classifier.best_estimator_

y_pred = rf_classifier.predict(X_test)

print('model params:', rf_classifier.get_params())
print()
print()
# 6) Show metrics

accuracy = rf_classifier.score(X_test,y_test)
auc_score = roc_auc_score(y_test, y_pred) 

print(f'accuracy: {accuracy} - auc: {auc_score}')
print()
print()
# 7) Export model into BentoML

tag = bentoml.sklearn.save_model('ml_proyect', 
     rf_classifier,
     custom_objects={
        'DictVectorizer':dv
    })
print(tag)
print()
print('!!END!!')

#Model(tag="ml_proyect:s7orz7c4vkqlilhq")





