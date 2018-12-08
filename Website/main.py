# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 16:01:39 2018

@author: Gašper Rugelj
"""

import os
import json

import flask
import results
app = flask.Flask('__name__', template_folder='html')

@app.route('/get_results')
def aoc_2018(*args, **kwargs):
    total = results.get_results(convert_ts=True)
    data = total.to_dict(orient='records')
    columns = list(total.columns)
    response = json.dumps(dict(data = data, columns=columns))
#    total = json.dumps(total.to_dict(orient='records'))
    return response.replace('NaN', 'null').replace('NaT', '')

@app.route('/')
def index(name='AoC 2018'):
    return flask.render_template('template.html', name=name)

if __name__ == '__main__':
    app.run(port=5008, host='0.0.0.0', debug=True)