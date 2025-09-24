import pandas as pd

def read_json_file(path):
    data = pd.read_json(path)    
    return data

def add_two_to_sepal_length(path,store_path):
    data = read_json_file(path)
    data['sepalLength']*=2
    data.to_json(store_path,orient="records")

    return data