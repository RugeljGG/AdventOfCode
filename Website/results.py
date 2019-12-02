# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 10:50:46 2018

@author: Gašper Rugelj
"""

import json

import pandas as pd
import requests

with open('cookie') as file:
    cookie = json.load(file)
url = 'https://adventofcode.com/2018/leaderboard/private/view/118799.json'

def get_results(convert_ts=False):


    r = requests.get(url, cookies=cookie)

    max_level = min((pd.to_datetime('today')-pd.to_datetime('2018-11-30')).days, 25)
    results = r.json()
    total = []
    for result in results['members'].values():
        member = result['id']
        name = result['name']
        score = result['local_score']
        levels = result['completion_day_level']
        row = [member, name, score]
        for level in range(1, max_level+1):
            times = levels.get(str(level))
            if times is None:
                row += [None, None]
            else:
                for stage in ['1', '2']:
                    t = times.get(stage)
                    if t is not None:
                        row.append(int(t.get('get_star_ts')))
                    else:
                        row.append(None)
        total.append(row)


    columns = ['ID', 'Name', 'Score']
    icol = 3 # first time col for conversion
    for i in range(1, max_level+1):
        columns+='{0}a,{0}b'.format(i).split(',')


    def timezone(series):
        s = pd.to_datetime(series, unit='s')
        s = s.dt.tz_localize('UTC').dt.tz_convert('CET')
        s = s.dt.strftime('%#d.%m. %H:%M:%S')
        return s

    total = pd.DataFrame(total, columns=columns)
    if convert_ts:
        total.iloc[:, icol:] = total.iloc[:, icol:].apply(timezone)
    #total.iloc[:, icol:] = total.iloc[:, icol:].apply(pd.to_datetime, unit='s')
    total = total.sort_values('Score', ascending=False)

    return total

if __name__ == '__main__':
    total = get_results(convert_ts=True)