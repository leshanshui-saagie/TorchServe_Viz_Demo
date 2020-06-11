import os
import json
import warnings, logging
import subprocess
import importlib
import requests
from flask import Flask, flash, redirect, render_template, request, session, abort, jsonify, request, current_app, Response
from hdfs import InsecureClient


logging.basicConfig(level=logging.INFO, format='%(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


application = Flask(__name__)


@application.route('/')
def index():
    logger.info('Visited index page')
    health = os.popen("curl -k https://research-workspace.a3.saagie.io/app/c5d028a6-713e-4d8f-a871-46f86367c0c8/8080/ping/").read().strip()
    models = os.popen("curl -k https://research-workspace.a3.saagie.io/app/c5d028a6-713e-4d8f-a871-46f86367c0c8/8081/models/").read().strip()
    health = health.replace('\n', '').replace(' ', '').split('"')[3]
    models = models.replace('\n', '').replace(' ', '')
    model_names = ' \n '.join([d['modelName'] for d in json.loads(s=models)['models']])
    return render_template('viz.html',**locals())

if __name__ == '__main__':
    application.run(host='0.0.0.0', port=8078)
