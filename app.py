from flask import Flask, render_template, request
import pickle
import recommender
import pandas as pd
from recommender import contents_based_recommender

app = Flask(__name__)
model=pickle.load(open('model.pkl','rb'))

@app.route('/') # To render Homepage
def home_page():
    return render_template('index.html')

@app.route('/submit',methods=['POST','GET'])
def submit():
     #Taking inputs from html page to python code;
     name = request.form["genrename"]
     n_books = int(request.form["books_count"])
     result = recommender.contents_based_recommender(name,n_books)
     #returning values to html page
     return render_template('index.html',mk = result)

if __name__ == '__main__':
    app.run()