#!/usr/bin/python3
import os
from flask import Flask, jsonify, redirect, request
from flask_jsonrpc import JSONRPC
from api.pharmacy import pharmacy
import settings
from settings import logger, env


app = Flask(__name__)

jsonrpc = JSONRPC(app, '/api', enable_web_browsable_api=True)
jsonrpc.register_blueprint(app, pharmacy, url_prefix='/v1', enable_web_browsable_api=True)

@jsonrpc.method('App.index')
def index() -> str:
    return 'Welcome to Pharmacies Finder'

if __name__ == '__main__':
    debug = env.bool('DEBUG', True)
    logger.info("Start App Flask")
    context = None
    if env.bool('SSL_ENABLED', False):
        #TODO: add certificate and key files for production purpose
        context = ('path/to/file.crt', 'path/to/file.key')
    
    app.run(debug=debug, host='0.0.0.0', ssl_context=context)