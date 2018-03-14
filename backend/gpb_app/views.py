from flask import render_template, jsonify
from gpb_app.app import app
from gpb_app.controllers import question

# import logging
# from logging.handlers import RotatingFileHandler


@app.route('/')
def index():
    return render_template('app.html')


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    """
    see frontend/src/router/index.js
    """
    return render_template('app.html')


@app.route('/question/<string:query>',)
def send_query(query):
    """
    <string:#> is a flask converter
    http://exploreflask.com/en/latest/views.html#url-converters
    handles inputs from a form
    """
    processed_query = question.QuestionHandler(query)
    answer = processed_query.to_output()
    return jsonify(answer)
