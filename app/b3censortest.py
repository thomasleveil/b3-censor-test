# -*- encoding: utf-8 -*-
import os
from flask import Flask
from flask.templating import render_template

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

@app.route('/')
def index():
    with open(os.path.join(os.path.dirname(__file__), 'etc/plugin_censor.xml')) as default_config_file:
        default_config_content = default_config_file.read()
    return render_template('index.html', config_content=default_config_content)

if __name__ == '__main__':
    app.debug = True
    app.run()
