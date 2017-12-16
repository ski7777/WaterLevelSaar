#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#

import urllib.request
import os
import json


def getStationList():
    url = 'http://www.umweltserver.saarland.de/extern/wasser/Daten.js'
    raw = urllib.request.urlopen(url).read().decode('utf-8', errors='ignore').splitlines()
    rawList = list(filter(lambda x: x != '' and x != ' ', raw))

    data = {}
    for line in rawList:
        line = line.split("(")[1].split(")")[0]
        stationID = int(line.split(",")[2].split("'")[1])
        stationData = {}
        stationData['city'] = line.split(",")[4].split("'")[1]
        stationData['river'] = line.split(",")[5].split("'")[1]
        data[stationID] = stationData

    return(data)
