import os

from flask import Flask, Response, request, render_template, flash, redirect, session, url_for, json, make_response
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)

import models

# edit from new comp

@app.route('/')
def index():
	return 'test'
	#return render_template('index.html')

@app.route('/test_index')
def test():
	return ''
	#return render_template('base.html')

@app.route('/test_index_for_temp_page')
def test_index():
	return render_template('index.html')
	
if __name__ == '__main__':
	app.run()