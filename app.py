from hashlib import new
from newspaper import article
import numpy as np
from flask import Flask, request, render_template
from flask_cors import CORS
import os
import joblib
import pickle
import flask
import os
import newspaper
from newspaper import Article
import urllib
import nltk
nltk.download('punkt')

# loading flask and assigning the model variable
app = Flask(__name__)
CORS(app)
app= flask.Flask(__name__,template_folder='templates')

with open('model.pkl','rb') as handle:
    model = pickle.load(handle)


@app.route('/')
def main():
    return render_template("index.html")


@app.route('/prediction', methods=['GET', 'POST'])
def prediction():
        return render_template("prediction.html")

# receiving the input url from the user and using web scrapping to extract the news content
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    url = request.get_data(as_text=True)[5:]
    url= urllib.parse.unquote(url) # parsed url 
    article = Article(str(url)) # created instance of an article
    print(article)
    article.download() 
    article.parse()
    article.nlp() # applied nlp on article
    news =article.summary
    # passing the news article to the model and returning whether it is Fake or real
    pred=model.predict([news])
    print(pred[0])
    return render_template("prediction.html",prediction_text="This news seems to be {}".format(pred[0]))

if __name__ == '__main__':
    port=int(os.environ.get('PORT',5000))
    app.run(port=port,debug=True,use_reloader=False)