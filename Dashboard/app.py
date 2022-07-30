from crypt import methods
from flask import Flask, render_template, request, jsonify
import nltk
import pickle
from nltk.corpus import stopwords
import re
from nltk.stem.porter import PorterStemmer

app = Flask(__name__)
ps = PorterStemmer()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods = ['GET', 'POST'])
def predict():
    #load model in here
    model_1 = pickle.load(open('model_1.pkl', 'rb'))
    #get news UI
    #predict to HTML
    return render_template("index.html")

if __name__ == "__main__":
    app.run()