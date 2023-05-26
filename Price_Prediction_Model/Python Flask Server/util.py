#Python Flask Server

#util.py conatins all the core routines

#importing required libraries
import pickle
import json
import numpy as np

__locations = None
__data_columns = None
__model = None

#defining a function to get the estimated price
def get_estimated_price(location,sqft,bhk,bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0],2)

#defining a function to load the saved artifacts i.e. banglore_home_prices_model.pickle and columns.json
def load_saved_artifacts():
    print("loading saved artifacts...start")
    global  __data_columns
    global __locations

    #opening, reading and loading columns.json
    with open("/Users/lokesh/VS Code/Price_Prediction_Model/Python Flask Server/Artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]  # first 3 columns are sqft, bath, bhk

    global __model
    if __model is None:
        #opening, reading and loading banglore_home_prices_model.pickle
        with open('/Users/lokesh/VS Code/Price_Prediction_Model/Python Flask Server/Artifacts/banglore_home_prices_model.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")

def get_location_names():
    return __locations

def get_data_columns():
    return __data_columns

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('1st Phase JP Nagar',1000, 3, 3))
    print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
    print(get_estimated_price('Kalhalli', 1000, 2, 2)) # other location
    print(get_estimated_price('Ejipura', 1000, 2, 2))  # other location