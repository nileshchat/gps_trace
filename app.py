from flask import Flask, render_template, request
from geo_plot import process

app = Flask(__name__)


@app.route('/')
def home():
	return render_template('index.html') # 'Project running'


@app.route('/save', methods=['POST'])
def process_view():
	start = request.form['start']
	finish = request.form['finish']
	process(start, finish)
	return render_template('map.html')
