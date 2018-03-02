from flask import render_template, jsonify
import requests
from random import randint
from gpb_app.app import app
from gpb_app.controllers import question

import logging
from logging.handlers import RotatingFileHandler


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    if app.debug:
        return requests.get('https://localhost:8080/{}'.format(path)).text
    return render_template("index.html")


@app.route('/question/<string:query>',)
def send_query(query):
    """
    <string:#> is a flask converter
    http://exploreflask.com/en/latest/views.html#url-converters
    handles inputs from html files
    """
    processed_query = question.QuestionHandler(query)
    answer = processed_query.to_json()
    return jsonify(answer)


@app.route('/api/random')
def random_number():
    response = {
        'randomNumber': randint(1, 100)
    }
    return jsonify(response)
