
from __future__ import print_function
from flask import Flask, render_template, make_response
from flask import redirect, request, jsonify, url_for

import io
import os
import uuid
import json
import csv


app = Flask(__name__, template_folder='website')
app.secret_key = 's3cr3t'
app.debug = True
app._static_folder = os.path.abspath("website/")

@app.route('/', methods=['GET'])
def index():
    title = 'Create the input'
    return render_template('index.html',
                           title=title)

@app.route('/game', methods=['GET'])
def game():
    title = 'Create the input'
    return render_template('game.html',
                           title=title)

@app.route('/endGame', methods=['GET'])
def game1():
   title = 'Create the input'
   return render_template('endGame.html',
                          title=title)

@app.route('/level2', methods=['GET'])
def game2():
   title = 'Create the input'
   return render_template('level2.html',
                          title=title)                           
                          


@app.route('/senddata', methods = ['POST'])
def post_javascript_data():
    data=request.data
    dataDict = json.loads(data)
    package = zip(*dataDict.items())
    csv_columns = ('')
    csv_file = "response.csv"
    print(type(dataDict))
    for key, value in dataDict.items():
        print("key:", key)
        print("value",value)
    with open('response.csv', 'a') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(csv_columns)
        for data in package:
            writer.writerow(data)
        csvfile.close()    
        print("done")
    return "Done"



def create_txt(text):
    with open('data.txt', 'a') as file:
        file.write(text+"\n")
    return 'data'

def get_file_content(uuid):
    with open('images/'+uuid+'.csv', 'r') as file:
        return file.read()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)