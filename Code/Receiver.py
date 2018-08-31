#!/usr/bin/env python
import pika
import random
import time
import sys
import datetime
import QoECurve


'''
MsgBroker Configuration
'''
max_priority = 250
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
c_properties  = dict()
c_properties['x-max-priority'] = max_priority
channel.queue_declare(queue='hello', durable=False, arguments = c_properties)

'''
Msg Handler
'''

def datahandler(body):
    # print(str(body))
    message_body = str(body).split()
    message_body[0] = message_body[0].strip('b\'')
    message_body[1] = message_body[1].strip('\'')
    # print(message_body[0])
    now_time = int(round(time.time() * 1000))
    e2e_latency = now_time - int(message_body[0]) + int(message_body[1])
    sa, sb = QoECurve.QoECurve(e2e_latency)
    print(sa)
    time.sleep(0.005)


def callback(ch, method, properties, body):
    #print(" [x] Received " + str(body) + ' ' + str(datetime.datetime.now()))
    datahandler(body)
    channel.basic_ack(delivery_tag = method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback,
                      queue='hello'
                      )
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
