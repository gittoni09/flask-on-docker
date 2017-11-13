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
    return render_template('c2f.html', x=zipped)

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
    return render_template('f2c.html', x=zipped)
	
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name) 

@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' % username

@app.errorhandler(404)
def not_found(error):
    return render_template('error404.html'), 404

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')

