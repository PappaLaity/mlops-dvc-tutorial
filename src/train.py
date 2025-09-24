import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

from src.prepocess import read_json_file

def split_data(path):
    data = read_json_file(path)
    # transform Categori to Numeric
    data['species'] = data['species'].replace({'virginica': 0, 'setosa': 1, 'versicolor': 2})
    y = data['species']
    X = data.drop(columns=['species'])
    return train_test_split(X, y, test_size=0.3, random_state=42)

def train_lr_model(X_train,y_train):
    model = LogisticRegression()
    model.fit(X_train,y_train)
    return model

def evaluate_lr_model(y_pred,y_test):
    acc = accuracy_score(y_pred,y_test)
    return acc