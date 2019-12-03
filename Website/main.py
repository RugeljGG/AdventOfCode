# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 16:01:39 2018

@author: Gašper Rugelj
"""

import json

import flask
import results
app = flask.Flask('__name__', template_folder='html')

@app.route('/get_results/<year>')
def result_page(year, *args, **kwargs):
    total = results.get_results(year=year, convert_ts=True)
    data = total.to_dict(orient='records')
    columns = list(total.columns)
    response = json.dumps(dict(data = data, columns=columns))
    return response.replace('NaN', 'null').replace('NaT', '')

@app.route('/')
@app.route('/<year>')
def index(year=2019):
    if year not in [2017, 2018, 2019]:
        year = 2019
    name = 'AoC {}'.format(year)
    return flask.render_template('template.html', name=name, year=year)

if __name__ == '__main__':
    app.run(port=5008, host='0.0.0.0', debug=True)