#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#


class Debug():
    pass


from .StationGenerator import getStationList
import urllib.request
import datetime

baseURL = 'https://iframe01.saarland.de/extern/wasser/daten/'
URLending = '.txt'


def getStationData(id):
    try:
        url = baseURL + str(id) + URLending
        raw = urllib.request.urlopen(url).read().decode('utf-8', errors='ignore').splitlines()
        rawList = list(filter(lambda x: x != '' and x != ' ', raw))

        meta = {}
        meta['id'] = rawList[0].split(';')[0]
        meta['location'] = rawList[0].split(';')[1].replace('"', '')
        meta['river'] = rawList[0].split(';')[2].replace('"', '')
        rawList.pop(0)

        data = {}
        for x in rawList:
            date = x.split(';')[0].split(".")
            time = x.split(';')[1].split(":")
            epoch = int(datetime.datetime(int(date[2]), int(date[1]), int(date[0]), int(time[0]), int(time[1])).strftime('%s'))
            level = int(x.split(';')[2])
            if level != -9999:
                data[epoch] = level
    except:
        data = {}
        meta = {}
    return(data, meta)
