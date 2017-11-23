#!/usr/bin/python
import os
from datetime import datetime
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# if request.headers.getlist("X-Forwarded-For"):
   # ip = request.headers.getlist("X-Forwarded-For")[0]
# else:
   # ip = request.remote_addr
#https://stackoverflow.com/questions/12770950/flask-request-remote-addr-is-wrong-on-webfaction-and-not-showing-real-user-ip?noredirect=1&lq=1
#OK: https://stackoverflow.com/questions/3759981/get-ip-address-of-visitors
   
#Print host name for debugging purposes
hostname = os.environ['HOSTNAME']
print "Hostname: ", hostname

@app.route('/')
def index():
    currentdatetime = datetime.now()
    clientIP = request.remote_addr
    print request.environ['REMOTE_ADDR']
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
    return render_template('c2f.html', x=zipped, hostname=hostname, currentdatetime=currentdatetime )

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
    return render_template('f2c.html', x=zipped, hostname=hostname, currentdatetime=currentdatetime )

@app.route('/guesser')
def guesser():
    currentdatetime = datetime.now()
    return render_template('guesser.html', hostname=hostname, currentdatetime=currentdatetime )
	
@app.route('/missing')
def missing():
    currentdatetime = datetime.now()
    return render_template('missing.html', hostname=hostname, currentdatetime=currentdatetime )
	
@app.errorhandler(404)
def not_found(error):
    currentdatetime = datetime.now()
    return render_template('error404.html', hostname=hostname, currentdatetime=currentdatetime ), 404

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')

