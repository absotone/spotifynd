import pickle 
import numpy as np 


"""
    Load model from file
"""
def loadModel(path):
    return pickle.load(open(path,"rb"))

"""
    Convert the input data points into something acceptable by the model
"""
def getDataList(danceability, energy, instrumentalness, key, liveness, speechiness, tempo, valence):
    l = [danceability, energy, instrumentalness, key, liveness, speechiness, tempo, valence]
    floatList =  [float(x) for x in l]
    return np.array(floatList).reshape(1, -1)

"""
    Get Predicted Label (i.e Cluster Center) of the input Values
"""
def getLabel(model, inputValues):
    return model.predict(inputValues)[0]


