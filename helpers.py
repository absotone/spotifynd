import pickle 
import numpy as np 
import pandas as pd


"""
    Load Dataset
"""
df = pd.read_csv("data/min.csv")



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

"""
    Get songs with the same label
"""
def getSongsWithLabel(label,numSongs=5):
    label = int(label)
    label_df = df[df["label"] == label]
    return  (label_df.sample(numSongs)["name"])[:numSongs]



