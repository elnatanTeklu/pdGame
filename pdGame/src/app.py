
from __future__ import print_function
from flask import Flask, render_template, make_response
from flask import redirect, request, jsonify, url_for, send_file


import io
import os
import uuid
import json
import csv



#create global variables
demogDict = {}





app = Flask(__name__, static_url_path='', static_folder='static', template_folder='website')
app.secret_key = 's3cr3t'
app.debug = True
app._static_folder = os.path.abspath("website/")

@app.route('/', methods=['GET'])
def index():
    title = 'Create the input'
    return render_template('index.html',
                           title=title)


@app.route('/game1Demographics', methods=['GET'])
def game1Demographics():
    title = 'Create the input'
    return render_template('game1Demographics.html',
                           title=title)

@app.route('/game', methods=['GET'])
def game():
    title = 'Create the input'
    return render_template('game.html',
                           title=title)


@app.route('/game2Demographics', methods=['GET'])
def game2Demographics():
    title = 'Create the input'
    return render_template('game2Demographics.html',
                           title=title)                                            
                         



@app.route('/game2', methods=['GET'])
def game2():
    title = 'Create the input'
    return render_template('game2.html',
                           title=title)  



@app.route('/basicDemographic', methods=['GET'])
def basicDemographic():
    title = 'Create the input'
    return render_template('basicDemographic.html',
                           title=title)


@app.route('/basicGame', methods=['GET'])
def basicGame():
    title = 'Create the input'
    return render_template('basicGame.html',
                           title=title)


@app.route('/basicPicturesDemographic', methods=['GET'])
def basicPicturesDemographic():
    title = 'Create the input'
    return render_template('basicPicturesDemographic.html',
                           title=title)      


@app.route('/basicGamePictures', methods=['GET'])
def basicGamePictures():
    title = 'Create the input'
    return render_template('basicGamePictures.html',
                           title=title)
@app.route('/imagesWithNames', methods=['GET'])
def imagesWithNames():
    title = 'Create the input'
    return render_template('imagesWithNames.html',
                           title=title)

@app.route('/game4Demographic', methods=['GET'])
def game4Demographic():
    title = 'Create the input'
    return render_template('game4Demographic.html',
                           title=title)   

@app.route('/game4', methods=['GET'])
def game4():
    title = 'Create the input'
    return render_template('game4.html',
                           title=title)

@app.route('/game5Demographic', methods=['GET'])
def game5Demographic():
    title = 'Create the input'
    return render_template('game5Demographic.html',
                           title=title)   

@app.route('/game5', methods=['GET'])
def game5():
    title = 'Create the input'
    return render_template('game5.html',
                           title=title)



@app.route('/stochasticDemographic', methods=['GET'])
def stochasticDemographic():
    title = 'Create the input'
    return render_template('stochasticDemographic.html',
                           title=title)  

@app.route('/stochastic', methods=['GET'])
def stochastic():
    title = 'Create the input'
    return render_template('stochastic.html',
                           title=title)   



@app.route('/stochasticLastDemographic', methods=['GET'])
def stochasticLastDemographic():
    title = 'Create the input'
    return render_template('stochasticLastDemographic.html',
                           title=title)  

@app.route('/stochasticLast', methods=['GET'])
def stochasticLast():
    title = 'Create the input'
    return render_template('stochasticLast.html',
                           title=title)




@app.route('/stochasticBasicDemographic', methods=['GET'])
def stochasticBasicDemographic():
    title = 'Create the input'
    return render_template('stochasticBasicDemographic.html',
                           title=title)  

@app.route('/stochasticBasic', methods=['GET'])
def stochasticBasic():
    title = 'Create the input'
    return render_template('stochasticBasic.html',
                           title=title)   




@app.route('/stochasticFirstPicturesDemographic', methods=['GET'])
def stochasticFirstPicturesDemographic():
    title = 'Create the input'
    return render_template('stochasticFirstPicturesDemographic.html',
                           title=title)  

@app.route('/stochasticFirstPictures', methods=['GET'])
def stochasticFirstPictures():
    title = 'Create the input'
    return render_template('stochasticFirstPictures.html',
                           title=title)    




@app.route('/stochasticLastPicturesDemographic', methods=['GET'])
def stochasticLastPicturesDemographic():
    title = 'Create the input'
    return render_template('stochasticLastPicturesDemographic.html',
                           title=title)  

@app.route('/stochasticLastPictures', methods=['GET'])
def stochasticLastPictures():
    title = 'Create the input'
    return render_template('stochasticLastPictures.html',
                           title=title)  



@app.route('/stochasticBasicPicturesDemographic', methods=['GET'])
def stochasticBasicPicturesDemographic():
    title = 'Create the input'
    return render_template('stochasticBasicPicturesDemographic.html',
                           title=title)  

@app.route('/stochasticBasicPictures', methods=['GET'])
def stochasticBasicPictures():
    title = 'Create the input'
    return render_template('stochasticBasicPictures.html',
                           title=title)                                            


                           
                                            

@app.route('/downloads', methods=['GET'])
def downlaods():
   title = 'Create the input'
   return render_template('downloads.html',
                          title=title)
@app.route('/downloadcsv/<password>')
def return_csv(password):
	if(password!="Pris527"):
		return "False Password"
	try:
		return send_file('response.csv',mimetype='text/csv',as_attachment=True , attachment_filename='response.csv')
	except Exception as e:
		return str(e)						  

@app.route('/gameResults', methods=['GET'])
def game3():
   title = 'Create the input'
   return render_template('gameResults.html',
                          title=title) 


@app.route('/endGame', methods=['GET'])
def game1():
   title = 'Create the input'
   return render_template('endGame.html',
                          title=title)


                          
@app.route('/level2', methods=['GET'])
def game9():
    title = 'Create the input'
    return render_template('level2.html',
                           title=title) 

@app.route('/senddemogdata', methods = ['POST'])
def post_javascript_demogdata():
    demogdata=request.data
    global demogDict
    demogDict = json.loads(demogdata)
##    print("demogdictfirst")
##    print(demogDict)
##    print("sending demographic data")
    return "demogDictDone"


@app.route('/senddata', methods = ['POST'])
def post_javascript_data():
    data=request.data
    txtData = request.data
    txtDict = json.loads(txtData)
    strJson = json.dumps(txtDict)
    create_txt(strJson)
    dataDict = json.loads(data)
##    print("demogDict")
##    print(demogDict)
    dataDict.update(demogDict)
    countDict = {"user number":user_count()}
    dataDict.update(countDict)
    package = zip(*dataDict.items())
    csv_columns = ('')
    csv_file = "response.csv"
    print("Type of dataDict is")
    print(type(dataDict))
    print("Type of package is")
    print(type(package))
    for key, value in dataDict.items():
        print("key:", key)
        print("value",value)
        csv_columns += key
    with open('response.csv', 'a') as csvfile:
        writer = csv.writer(csvfile)
##      writer.writerow(csv_columns)
        for data in package:
            writer.writerow(data)
        csvfile.close()    
        print("test")
        
    return "Done"

def create_txt(text):

    with open('data.txt', 'a+') as file:
        file.write(text+ ',' + "\n" )
    return 'data'

def get_file_content(uuid):
    with open('images/'+uuid+'.csv', 'r') as file:
        return file.read()
        

@app.route('/metaData', methods = ['POST'])
def post_javascript_metaData():
    txtData = request.data
    txtDict = json.loads(txtData)
    strJson = json.dumps(txtDict)
    createMetaData_txt(strJson)
   

    return "metaData sent"

def createMetaData_txt(text):

    with open('metaData.txt', 'a+') as file:
        file.write(text+ ',' + "\n" )
    return 'metaData'




def user_count():
    file_name = "userCount.txt"

    try:
        with open(file_name, "r+") as f:
            data = f.read().strip()
            output = (int)(data) + 1
            f.seek(0)
            f.write((str)(output))
            f.truncate()
    except:
        with open(file_name, "w") as f:
            output = "1"
            f.seek(0)
            f.write((str)(output))
            f.truncate()
    print(output)        
    return output
    
        

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

