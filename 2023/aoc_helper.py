# -*- coding: utf-8 -*-

import os
import requests

with open('../token.txt', 'r') as file:
    token = next(file)

def get_input(day, year=2023, force=False):

    f_path = r'day{}.txt'.format(day)
    if not force and os.path.exists(f_path):
        print("Input already exists, generating it from file")
        with open(f_path, 'r') as file:
            return file.read()

    else:
        url = 'https://adventofcode.com/{}/day/{}/input'.format(year,day)
        r = requests.get(url, cookies={'session':token})
        with open(f_path, 'w') as file:
            print(r.text, file=file)
        return r.text