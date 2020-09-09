#!/usr/bin/python3
import os
from flask import Flask, jsonify, redirect, request
from flask_jsonrpc import JSONRPC
import settings
from settings import logger, env
from controllers.pharmacy import Pharmacy


app = Flask(__name__, instance_relative_config=True)

jsonrpc = JSONRPC(app, '/api', enable_web_browsable_api=True)

@jsonrpc.method('App.index')
def index() -> str:
    return 'Welcome to Pharmacies Finder'

pharmacy = Pharmacy()
jsonrpc.register(pharmacy.SearchNearestPharmacy)

if __name__ == '__main__':
    debug = env.bool('DEBUG', True)
    logger.info("Start App Flask")
    context = None
    if env.bool('SSL_ENABLED', False):
        #TODO: add certificate and key files for production purpose
        context = ('path/to/file.crt', 'path/to/file.key')
    
    app.run(debug=debug, host='0.0.0.0', ssl_context=context)