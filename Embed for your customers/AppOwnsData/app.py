# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

from services.pbiembedservice import PbiEmbedService
from utils import Utils
from flask import Flask, render_template, send_from_directory,redirect, url_for, request
import json
import os


# Initialize the Flask app
app = Flask(__name__)

# Load configuration
app.config.from_object('config.BaseConfig')

@app.route('/')
def index():
    '''Returns a static HTML page'''

    return render_template('index.html')

@app.route('/newcampaign')
def newcampaign():
    return render_template('newcampaign.html')

@app.route('/adminlogin',methods=['GET','POST'])
def login():
    error=None
    if request.method=='POST':
        print(request.form['username'])
        if request.form['username'] != app.config['ADMIN_USER'] or request.form['password'] != app.config['ADMIN_PASS']:
            error = 'Usuario o contraseña invalido, Intente nuevamente.'
        else:
            return redirect(url_for('newcampaign'))  
    return render_template('login.html',error=error)

@app.route('/getembedinfo', methods=['GET'])
def get_embed_info():
    '''Returns report embed configuration'''

    config_result = Utils.check_config(app)
    if config_result is not None:
        return json.dumps({'errorMsg': config_result}), 500

    try:
        embed_info = PbiEmbedService().get_embed_params_for_single_report(app.config['WORKSPACE_ID'], app.config['REPORT_ID'])
        return embed_info
    except Exception as ex:
        return json.dumps({'errorMsg': str(ex)}), 500

@app.route('/favicon.ico', methods=['GET'])
def getfavicon():
    '''Returns path of the favicon to be rendered'''

    return send_from_directory(os.path.join(app.root_path, 'static'), 'img/favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
    app.run()