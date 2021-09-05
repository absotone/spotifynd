from sys import displayhook
from flask import Flask, render_template, request
import pickle
from numpy import mod
import pandas as pd 

from helpers import *

model = loadModel("models/simplemodel.sav")


app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict/", methods = ["GET","POST"])
def predict():
    if request.method == "POST":
        
        danceability = request.form.get("danceability")
        energy = request.form.get("energy")
        instrumentalness = request.form.get("instrumentalness")
        key = request.form.get("key")
        liveness = request.form.get("liveness")
        speechiness = request.form.get("speechiness")
        tempo = request.form.get("tempo")
        valence = request.form.get("valence")

        label = getLabel(model,
                        getDataList(danceability, energy, instrumentalness, key, liveness, speechiness, tempo, valence))

        return render_template("predict.html",label = str(label), displayForm = False)

    else:
        return render_template("predict.html", label = "", displayForm = True)