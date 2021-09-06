from sys import displayhook
from flask import Flask, render_template, request
import pickle
from numpy import mod
import pandas as pd 
from getsongdetails import SongData
import creds
from helpers import *

model = loadModel("models/complexmodel.sav")

songDataLoader = SongData(creds.CLIENT_ID,creds.CLIENT_SECRET)

NUM_SONGS_SHOW = 10


app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)

@app.route("/", methods = ["GET","POST"])
def predict():
    if request.method == "POST":
        
        song_id = request.form.get("song_id")
        song_features = songDataLoader.getSongFeatures(song_id)

        label = getLabel(model,
                        song_features)

        
        indexListRet = getSongsWithLabel(label,NUM_SONGS_SHOW)
        return render_template("index.html",label = str(label), displayForm = False, indexList = indexListRet)

    else:
        return render_template("index.html", label = "", displayForm = True, indexListRet = [])

if __name__ == "__main__":
    app.run(debug=True)