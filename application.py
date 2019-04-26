from flask import Flask,request,jsonify
import sys
import time
# import MsSqlConnect
import json

#from zeep import Client
#import zeep
#from zeep.wsse.username import UsernameToken

#client = Client('https://ws.staging.training.gov.au/Deewr.Tga.WebServices/OrganisationServiceV7.svc?wsdl', wsse=UsernameToken('WebService.Read', 'Asdf098'))

import pyodbc

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!  pyodbc again"