#!/usr/bin/env python
# coding=utf-8

import json

def json_reader(fullpath):
    # Opening JSON config file
    f = open(fullpath)
    # returns JSON object as a dictionary
    data = json.load(f)
    metadata = data['headers']
    # Closing file
    f.close()
    dict_data = {}
    for item in metadata:
        if item['enabled'] == 'Y': # only active values
            dict_data[str(item['key'])] = str(item['value'])
    return dict(dict_data)