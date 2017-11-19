#!/usr/bin/python
import os
from flask import Flask
from flask import render_template
app = Flask(__name__)

#Print host name for debugging purposes
hostname = os.environ['HOSTNAME']
print "Hostname: ", hostname

@app.route('/')
def index():
    return render_template('index.html', hostname=hostname )

@app.route('/c2f')
def c2f():
    celsiusList = []
    farenList = []
    for cel in range(-20,101,10):
        celsiusList.append(cel) 
        faren = ((cel/5)*9)+32
        farenList.append(faren)
        cel =+ 10
    zipped = zip(celsiusList, farenList)
    return render_template('c2f.html', x=zipped, hostname=hostname )

@app.route('/f2c')
def f2c():
    celsiusList = []
    farenList = []
    for faren in range(-20,221,10):
        farenList.append(faren) 
        celsi = (((faren-32)*5)/9)
        celsiusList.append(celsi)
        faren =+ 10
    zipped = zip(farenList, celsiusList)
    return render_template('f2c.html', x=zipped, hostname=hostname )

@app.route('/guesser')
def guesser():
    return render_template('guesser.html', hostname=hostname )
	
@app.route('/missing')
def missing():
    return render_template('missing.html', hostname=hostname )
	
@app.errorhandler(404)
def not_found(error):
    return render_template('error404.html', hostname=hostname ), 404

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')

