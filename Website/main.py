# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 16:01:39 2018

@author: Gašper Rugelj
"""

from collections import defaultdict as dd
from datetime import datetime
import json
import logging
from threading import Lock

import flask

import results
app = flask.Flask('__name__', template_folder='html')

LIMIT = 60 # don't refresh more often than every 60 seconds
FIRST_YEAR = 2015

now = datetime.now()
LAST_YEAR = now.year if now.month == 12 else now.year - 1

YEARS = range(FIRST_YEAR, LAST_YEAR+1)

@app.route('/get_results/<year>')
def result_page(year, *args, duration=False, **kwargs):
    if lock.acquire(timeout=10):
        if (datetime.now() - cache[duration][year]['ts']).seconds < LIMIT:
            response = cache[duration][year]['data']
            logging.info('Refresh too soon, using cache')
        else:
            total = results.get_results(year=year,
                                        convert_ts=True,
                                        duration=duration)

            if total is None: # something failed
                logging.error('Failed retrieving data, using cache')
                response = cache[duration][year]['data']

            else:
                data = total.to_dict(orient='records')
                columns = list(total.columns)
                ts = datetime.now()
                response = json.dumps(dict(data = data,
                                           columns=columns,
                                           ts=ts.strftime('%Y-%m-%d %H:%M')))
                response = response.replace('NaN', 'null')
                response = response.replace('NaT', '')
                cache[duration][year]['data'] = response
                cache[duration][year]['ts'] = ts

        lock.release()

    else:
        logging.warning("Can't acquire lock, returning cached response")
        response = cache[duration][year]['data']
    return response


@app.route('/get_duration/<year>')
def duration(year, *args, **kwargs):
    return result_page(year, duration=True)


@app.route('/')
@app.route('/<year>')
def index(year=YEARS[-1], duration=False):
    year=int(year)
    if year not in YEARS:
        year = YEARS[-1]
    links = '\r\n'.join(['<a href="/{y}">{y}</a>'.format(y=y) for y in YEARS if y!= year])
    name = 'AoC {}'.format(year)
    ts = cache[duration][year]['ts']
    prefix = 'get_duration/' if duration else 'get_results/'
    return flask.render_template('template.html',
                                 name=name,
                                 year=year,
                                 ts=ts,
                                 links=links,
                                 prefix=prefix)


@app.route('/duration')
@app.route('/duration/<year>')
def index_duration(year=YEARS[-1]):
    return index(year, duration=True)


if __name__ == '__main__':
    lock = Lock()
    cache = dd(lambda: dd(lambda: dict(ts=datetime.min, data=None)))
    app.run(port=5008, host='0.0.0.0', debug=True)