# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 10:50:46 2018

@author: Gašper Rugelj
"""

import pandas as pd
import requests

with open('../token.txt', 'r') as file:
    token = next(file)
    cookie= {'session':token}
url = 'https://adventofcode.com/{year}/leaderboard/private/view/118799.json'

def _timezone(series):
    s = pd.to_datetime(series, unit='s')
    s = s.dt.tz_localize('UTC').dt.tz_convert('CET')
    s = s.dt.strftime('%#d.%m. %H:%M:%S')
    return s


def formatter(i):
    if pd.isnull(i):
        return ''
    else:
        return '{:.0f}h {:02.0f}m {:02.0f}s'.format(i//3600, (i%3600)//60, (i%60))


def get_results(convert_ts=False, year=2019, duration=False):

    try:
        r = requests.get(url.format(year=year), cookies=cookie, timeout=5)
    except:
        return None
    e = pd.to_datetime('today')
    s = pd.to_datetime('{}-11-30'.format(year))
    max_level = min((e-s).days, 25)
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
            
            if duration:
                if times is None:
                    row.append(None)
                else:
                    t1 = times.get('1')
                    t2 = times.get('2')
                    if t1 is None or t2 is None:
                        row.append(None)
                    else:
                        t1_time = t1.get('get_star_ts')
                        t2_time = t2.get('get_star_ts')
                        row.append(int(t2_time)-int(t1_time))
                
            else:                
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
        if duration:
            columns.append('{0}b-{0}a'.format(i))
        else:
            columns+='{0}a,{0}b'.format(i).split(',')


    total = pd.DataFrame(total, columns=columns)
    if convert_ts:
        if duration: 
            total.iloc[:, icol:] = total.iloc[:, icol:].applymap(formatter)
        else:
            total.iloc[:, icol:] = total.iloc[:, icol:].apply(_timezone)
    #total.iloc[:, icol:] = total.iloc[:, icol:].apply(pd.to_datetime, unit='s')
    total = total.sort_values('Score', ascending=False)

    return total

if __name__ == '__main__':
    total = get_results(convert_ts=True)