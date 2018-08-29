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

Scheduler = 'EDF' #You can change it to 'QoE' or 'EDF'
RequestsNB_FILE = '' #Non-backend delay of requests. Default is NULL.
RequestsSL_FILE = '' #Time interval between this request and the next. Default is NULL.


requests = RequestGenerator.RequestsGenerator(RequestsNB_FILE)
sleep_time = RequestGenerator.RequestsSleep(RequestsSL_FILE)

rq_pri = []
rq_st = []
rq_end = []

if (Scheduler=='QoE'):
    rq_pri, rq_st, rq_end = PrioritySettings.OurPriSettings(requests)
else:
    rq_pri, rq_st, rq_end = PrioritySettings.EDFPriSeetings(requests)


rq_priority = []

for i in range(0, len(requests)):
    for j in range(0, len(rq_pri)):
        if (requests[i]<=rq_end[j] and requests[i]>=rq_st[j]):
            rq_priority.append(rq_pri[j])


#test pri
# for i in range(0, len(requests)):
#     print(rq_priority[i])
#test pri

#test request reader
# for i in range(0, len(requests)):
#     print (str(sleep_time[i]))
#test request reader


#test priority_settings#
# for i in range(0, len(rq_pri)):
#     print (str(rq_pri[i]))
# for i in range(0, len(rq_st)):
#     print (str(rq_st[i])+' '+str(rq_end[i]) + ' ' + str(rq_pri[i]))
#test priority_settings#


RequestSender.RequestSender(Scheduler, requests, rq_pri, sleep_time)

print('END')


