#!/usr/bin/python
import os
import socket
from datetime import datetime
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

#OK: https://stackoverflow.com/questions/3759981/get-ip-address-of-visitors
   
#Obtain hostname, if it exists 
try:
    hostname = socket.gethostname()
except:
    hostname = "No hostname"

@app.route('/')
def index():
    currentdatetime = datetime.now()
    clientIP = request.remote_addr
    remote_addr = request.environ['REMOTE_ADDR']
    return render_template('index.html', hostname=hostname, currentdatetime=currentdatetime, clientIP=clientIP )

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
    currentdatetime = datetime.now()
    clientIP = request.remote_addr
    remote_addr = request.environ['REMOTE_ADDR']
    return render_template('c2f.html', x=zipped, hostname=hostname, currentdatetime=currentdatetime, clientIP=clientIP )

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
    currentdatetime = datetime.now()
    clientIP = request.remote_addr
    remote_addr = request.environ['REMOTE_ADDR']
    return render_template('f2c.html', x=zipped, hostname=hostname, currentdatetime=currentdatetime, clientIP=clientIP )

@app.route('/guesser')
def guesser():
    currentdatetime = datetime.now()
    clientIP = request.remote_addr
    remote_addr = request.environ['REMOTE_ADDR']
    return render_template('guesser.html', hostname=hostname, currentdatetime=currentdatetime, clientIP=clientIP )
	
@app.route('/missing')
def missing():
    currentdatetime = datetime.now()
    clientIP = request.remote_addr
    remote_addr = request.environ['REMOTE_ADDR']
    return render_template('missing.html', hostname=hostname, currentdatetime=currentdatetime, clientIP=clientIP )

@app.route('/missingposition')
def missingpos():
    currentdatetime = datetime.now()
    clientIP = request.remote_addr
    remote_addr = request.environ['REMOTE_ADDR']
    return render_template('missingpos.html', hostname=hostname, currentdatetime=currentdatetime, clientIP=clientIP )
	
@app.errorhandler(404)
def not_found(error):
    currentdatetime = datetime.now()
    clientIP = request.remote_addr
    remote_addr = request.environ['REMOTE_ADDR']
    return render_template('error404.html', hostname=hostname, currentdatetime=currentdatetime, clientIP=clientIP ), 404

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')

