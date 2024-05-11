from ast import If
from email.utils import parsedate
import json
import urllib
import urllib
from urllib import response
from flask import Response
from flask import jsonify
from flask import Flask, render_template, request, make_response, redirect
import MyHTMLParser

parser = MyHTMLParser.MyHTMLParser()
# Parse data from source 1
contents = urllib.request.urlopen("https://lite.cnn.com/en").read()
parser.feed(contents.decode("utf-8"), "https://lite.cnn.com")
cnnData = parser.data

# Parse data from source 2
# parser.setLimit(2)
parser.clearData()
contents = urllib.request.urlopen("https://neuters.de/").read()
parser.feed(contents.decode("utf-8"), "https://neuters.de")
neutersData = parser.data

# Parse data from source 3
parser.setLimit(4)
parser.clearData()
contents = urllib.request.urlopen("https://sjmulder.nl/en/textonly.html").read()
parser.feed(contents.decode("utf-8"), "https://sjmulder.nl/en/textonly.html")
htData = parser.data

app = Flask(__name__, static_url_path='')

# @app.route('/')
# def root():
#     return app.send_static_file('bootstrap.html')
    
# @app.route('/index.html')
# def index():
#     return app.send_static_file('bootstrap.html')

@app.route('/')
def hello():
    source = request.cookies.get('rnagoormCookie')
    if source == None:
        source = '0'
    # print(source)
    
    return render_template('bootstrap.html', source=source, cnnData=cnnData, neutersData=neutersData, htData=htData)

@app.route('/getnews')
def getnews():
	contents = urllib.request.urlopen("https://sjmulder.nl/en/textonly.html").read()
	return Response(contents, status=200)

@app.route('/setcookie/<source>', methods = ['POST', 'GET'])
def setcookie(source):
    if (source == '0'):
        resp = make_response(redirect('/'))
        resp.delete_cookie('rnagoormCookie')
    if (source == '1'):
        resp = make_response(redirect('/'))
        resp.set_cookie('rnagoormCookie', '1')
    if (source == '2'):
        resp = make_response(redirect('/'))
        resp.set_cookie('rnagoormCookie', '2')
    if (source == '3'):
        resp = make_response(redirect('/'))
        resp.set_cookie('rnagoormCookie', '3')
   
    return resp

# @app.route('/getcookie')
# def getcookie():
#    source = request.cookies.get('source')
#    return '<h1>welcome '+source+'</h1>'

@app.errorhandler(404)
def not_found(error=None):
    return {'status': 404, 'message': 'Not Found: ' + request.url}, 404



if __name__ == '__main__':
    app.run(debug = True)