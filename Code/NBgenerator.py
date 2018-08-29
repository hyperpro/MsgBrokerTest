#!/usr/bin/env python
import pika
import random
import sys
import time
import datetime
import RequestGenerator
import RequestSender
import QoECurve
import PrioritySettings

RequestNum = 40

requests = []

for i in range(0, RequestNum):
    delay = random.randint(1000, 4800)
    requests.append(delay)

# for i in range(0, RequestNum/3*2):
#     delay = random.randint(1000, 2400)
#     requests.append(delay)

for i in range(0, RequestNum):
    print(requests[i])