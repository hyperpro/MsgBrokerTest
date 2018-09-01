#!/usr/bin/env python
import pika
import random
import sys
import time
import datetime

def RequestSender(scheduler, requests, priority, sleep_time):

    '''
    Initialize the message broker
    '''
    max_priority = 250
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    properties = dict()
    properties['x-max-priority'] = max_priority
    channel.queue_declare(queue='hello', durable=False, arguments=properties)


    '''
    Send out requests
    '''
    for i in range(0, len(requests)):

        #current_time = datetime.datetime.now() #start time
        m_priority = priority[i]
        # print (m_priority)
        message = str(int(round(time.time() * 1000))) + ' ' + str(requests[i])

        if scheduler == 'QoE':
            channel.basic_publish(exchange='',
                                  routing_key='hello',
                                  properties=pika.BasicProperties(delivery_mode=2, priority=m_priority),
                                  body=message,
                                  )
        elif scheduler == 'EDF':
            channel.basic_publish(exchange='',
                                  routing_key='hello',
                                  properties=pika.BasicProperties(delivery_mode=2, priority=m_priority),
                                  body=message,
                                  )
        elif scheduler == 'SL':
            channel.basic_publish(exchange='',
                                  routing_key='hello',
                                  properties=pika.BasicProperties(delivery_mode=2, priority=m_priority),
                                  body=message,
                                  )
        elif scheduler == 'FIFO':
            channel.basic_publish(exchange='',
                                  routing_key='hello',
                                  properties=pika.BasicProperties(delivery_mode=2, priority = 0),
                                  body=message,
                                  )
        # time.sleep(sleep_time[i])

    '''
    Close the connection
    '''
    connection.close()

    return 0