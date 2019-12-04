# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 16:01:39 2018

@author: Gašper Rugelj
"""

from datetime import datetime
import json
from threading import Lock

import flask

import results
app = flask.Flask('__name__', template_folder='html')

LIMIT = 60 # don't refresh more often than every 60 seconds
YEARS = ('2017', '2018', '2019')

@app.route('/get_results/<year>')
def result_page(year, *args, **kwargs):
    if lock.acquire(timeout=10):
        if (datetime.now() - cache[year]['ts']).seconds < LIMIT:
            response = cache[year]['data']
            print('Too soon, using cache')
        else:
            total = results.get_results(year=year, convert_ts=True)
            if total is None: # something failed
                print('Failed retrieving data, using cache')
                response = cache[year]['data']
            else:
                data = total.to_dict(orient='records')
                columns = list(total.columns)
                ts = datetime.now()
                response = json.dumps(dict(data = data, 
                                           columns=columns, 
                                           ts=ts.strftime('%Y-%m-%d %H:%M')))
                response = response.replace('NaN', 'null').replace('NaT', '')
                cache[year]['data'] = response
                cache[year]['ts'] = ts
        lock.release()
    else:
        print("Can't acquire lock")
        response = cache[year]['data']
    return response

@app.route('/')
@app.route('/<year>')
def index(year='2019'):
    if str(year) not in YEARS:
        year = '2019'
    name = 'AoC {}'.format(year)
    ts = cache[year]['ts']
    return flask.render_template('template.html', name=name, year=year, ts=ts)

if __name__ == '__main__':
    lock = Lock()
    cache = {year: dict(ts=datetime.min, data=None) for year in YEARS}
    app.run(port=5008, host='0.0.0.0', debug=True)