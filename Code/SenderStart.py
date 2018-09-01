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

Scheduler = 'QoE' #You can change it to 'QoE' or 'EDF' or 'FIFO' or 'SL'
RequestsNB_FILE = '' #Non-backend delay of requests. Default is NULL.
RequestsSL_FILE = '' #Time interval between this request and the next. Default is NULL.

avg_processing_time = 5.0
avg_consuming_time = 5.0

requests = RequestGenerator.RequestsGenerator(RequestsNB_FILE)
sleep_time = RequestGenerator.RequestsSleep(RequestsSL_FILE)

rq_pri = []
rq_st = []
rq_end = []

if (Scheduler=='QoE'):
    rq_pri, rq_st, rq_end = PrioritySettings.OurPriSettings(requests, avg_processing_time, avg_consuming_time)
elif (Scheduler == 'EDF'):
    rq_pri, rq_st, rq_end = PrioritySettings.EDFPriSettings(requests)
else:
    rq_pri, rq_st, rq_end = PrioritySettings.SLPriSettings(requests)


rq_priority = []

for i in range(0, len(requests)):
    classi = 0
    for j in range(0, len(rq_pri)):
        if ( (requests[i]<= rq_end[j]+0.0001) and (requests[i]>=rq_st[j]-0.0001) ):
            classi = j
            break

    rq_priority.append(rq_pri[classi])
    # print(str(requests[i]) + ' ' + str( rq_priority[i]) + ' ' + str(classi) + ' ' + str(len(rq_pri)) + str(rq_pri[250]))


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

# for i in range(0, len(requests)):
#     print(str(requests[i]) + ' ' + str( rq_priority[i] ))

# for i in range(0, 250):
#     print(str(rq_pri[i]) + ' ' + str(rq_st[i]) + ' ' + str(rq_end[i]) )

RequestSender.RequestSender(Scheduler, requests, rq_priority, sleep_time)

print('END')


