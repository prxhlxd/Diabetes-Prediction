import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pickle

data = pd.read_csv('diabetes.csv')
data = data.fillna(data.mean())
X = data.drop(columns='Outcome')
y = data['Outcome']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

with open("naive_bayes_model.pkl", "rb") as f:
    nb_model = pickle.load(f)

perceptron_model = pickle.load(open('perceptron_model.pkl' , 'rb'))

def process(data):
    model_type = data['model_type']
    input= np.array([[ data['glucose'], data['insulin'], data['bmi'],data['age'] ]])
    input = scaler.transform(input.reshape(1, -1))
    print(input)
    # Choose the model based on input
    if model_type == 'naive_bayes':
        prediction = nb_model.predict(input)
    elif model_type == 'perceptron':
        prediction = perceptron_model.predict(input)
    return prediction

#print("done")