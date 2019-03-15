#!/usr/bin/env python # -*- coding: UTF-8 -*-
import urllib2, sys, cgi
from flask import Flask, render_template, redirect, url_for,request
from flask import make_response

##form = cgi.FieldStorage()
address = form.getvalue('mydata') ##sys.argv[1]
key = ""
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    urlAddress = ''
    for word in address:
        for letter in word:
            lastLetter = letter
        if lastLetter == ',':
            urlAddress = urlAddress + word + ' +'
        else:
            urlAddress = urlAddress + word + '+'
    urlAddress = urlAddress[:-1] #take off unneeded +
    url = "https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s" % (urlAddress, key)
    response = urllib2.urlopen(url)
    json = response.read()
    return json

@app.route('/index.py', methods=['GET', 'POST'])
def geocode():
    #address = sys.argv[1]
    urlAddress = ''
    for word in address:
        for letter in word:
            lastLetter = letter
        if lastLetter == ',':
            urlAddress = urlAddress + word + ' +'
        else:
            urlAddress = urlAddress + word + '+'
    urlAddress = urlAddress[:-1] #take off unneeded +
    url = "https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s" % (urlAddress, key)
    response = urllib2.urlopen(url)
    json = response.read()
    return json

if __name__ == "__main__":
    app.run(debug = True)
