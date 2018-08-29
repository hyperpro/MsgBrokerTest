#!/usr/bin/env python

import math
import sys
import random

def RequestsGenerator(FilePath):
    requests = []
    isNull = (len(FilePath) == 0)
    if (isNull == True):
        FilePath = 'TemplateNonbackendDelayData.txt'

    f = open(FilePath,'r')
    for line in f.readlines():
        requests.append(int(line))
    f.close()

    return requests


def RequestsSleep(FilePath):
    requests = []
    isNull = (len(FilePath) == 0)
    if (isNull == True):
        FilePath = 'TemplateNonbackendDelayData.txt'

    f = open(FilePath,'r')
    for line in f.readlines():
        requests.append(0)
    f.close()

    return requests