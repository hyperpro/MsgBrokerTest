#!/usr/bin/env python

import sys
import math
import QoECurve


def PerformanceGain(nbd_a, num_a, nbd_b, num_b, avg_processing, avg_consuming):
    answer, slope = QoECurve.QoECurve(nbd_a + avg_consuming * num_a / 2.0 + avg_processing)
    answer = answer * (num_a + 0.0)
    answer2, slope = QoECurve.QoECurve(nbd_b + avg_consuming * num_a + avg_consuming * num_b / 2.0 + avg_processing)
    answer2 = answer2 * (num_b + 0.0)
    answer = answer + answer2

    answer2, slope = QoECurve.QoECurve(nbd_b + avg_consuming * num_b/2.0 + avg_processing)
    answer2 = answer2 * (num_b + 0.0)
    answer = answer - answer2
    answer2, slope = QoECurve.QoECurve(nbd_a + avg_consuming * num_b + avg_consuming * num_a/2.0 + avg_processing)
    answer2 = answer2 * (num_a + 0.0)
    answer = answer - answer2

    return answer

def OurPriSettings1(requests, avg_processing, avg_consuming):  # Our QoE Scheduler

    priority_level = 250
    max_value = max(requests)
    min_value = min(requests)
    req_num = len(requests)

    # print(str(max_value))
    # print(str(min_value))

    pri_range = (max_value - min_value) / (priority_level + 0.0)
    step = pri_range / 2.0

    rg_start = []
    rg_end = []
    rg_nbdelay = []
    rg_slope = []
    rg_qoe = []
    rg_priority = []
    rg_num = []
    st_value = min_value

    while (st_value < max_value):
        rg_start.append(st_value)
        st_value += step
        rg_nbdelay.append(st_value)

        qoe, slope = QoECurve.QoECurve(st_value)
        rg_slope.append(slope)
        rg_qoe.append(qoe)

        st_value += step
        rg_end.append(st_value)
        rg_priority.append(-1)

    for i in range(0, priority_level):
        class_num = 0
        for j in range(0, req_num):
            if ((rg_start[i] <= requests[j]+0.00001) and (rg_end[i]+0.00001 >= requests[j])):
                class_num = class_num + 1
        rg_num.append(class_num)

    # print(len(rg_priority))
    # tttt = 0
    # for i in range(0, priority_level):
    #     tttt += rg_num[i]
    #     print(str(rg_start[i]) + ' ' + str(rg_end[i]) + ' ' + str(rg_num[i]))
    #
    # print(tttt)

    # print (len(rg_num))
    # print (len(rg_start))
    # print (len(rg_end))
    # for i in range(0, len(rg_start)):
    #     print(str(i) + ' ' + str(rg_start[i]) + ' ' + str(rg_end[i]) + ' ' + str(i))
    # for i in range(0, priority_level):
    #     print(str(rg_start[i]) + ' ' + str(rg_end[i]) + ' ' + str(rg_slope[i]))

    wt_time = 0

    for i in range(0, priority_level):

        max_gain = -1.0
        max_class = -1

        for j in range(0, priority_level):
            if (rg_priority[j] == -1):
                gain_j = 0.0
                vote = 0
                for k in range(0, priority_level):
                    if (rg_priority[k] == -1):
                        gain_j += PerformanceGain(rg_nbdelay[j] + wt_time, rg_num[j], rg_nbdelay[k] + wt_time, rg_num[k],
                                                 avg_processing, avg_consuming)
                        if (gain_j > 0):
                            vote += 1

                if (vote > max_gain):
                    max_gain = vote
                    max_class = j
                # print(gain_j)
        # print(max_class)
        wt_time += avg_consuming * rg_num[max_class]
        rg_priority[max_class] = priority_level - i

    # print(str(len(rg_priority)))
    return rg_priority, rg_start, rg_end


def OurPriSettings(requests, avg_processing, avg_consuming):  # Our QoE Scheduler

    priority_level = 250
    max_value = max(requests)
    min_value = min(requests)
    req_num = len(requests)

    # print(str(max_value))
    # print(str(min_value))

    pri_range = (max_value - min_value) / (priority_level + 0.0)
    step = pri_range / 2.0

    rg_start = []
    rg_end = []
    rg_nbdelay = []
    rg_slope = []
    rg_qoe = []
    rg_priority = []
    rg_num = []
    st_value = min_value

    while (st_value < max_value):
        rg_start.append(st_value)
        st_value += step
        rg_nbdelay.append(st_value)

        qoe, slope = QoECurve.QoECurve(st_value)
        rg_slope.append(slope)
        rg_qoe.append(qoe)

        st_value += step
        rg_end.append(st_value)
        rg_priority.append(-1)

    for i in range(0, priority_level):
        class_num = 0
        for j in range(0, req_num):
            if ((rg_start[i] <= requests[j]+0.00001) and (rg_end[i]+0.00001 >= requests[j])):
                class_num = class_num + 1
        rg_num.append(class_num)

    # print(len(rg_priority))
    # tttt = 0
    # for i in range(0, priority_level):
    #     tttt += rg_num[i]
    #     print(str(rg_start[i]) + ' ' + str(rg_end[i]) + ' ' + str(rg_num[i]))
    #
    # print(tttt)

    # print (len(rg_num))
    # print (len(rg_start))
    # print (len(rg_end))
    # for i in range(0, len(rg_start)):
    #     print(str(i) + ' ' + str(rg_start[i]) + ' ' + str(rg_end[i]) + ' ' + str(i))
    # for i in range(0, priority_level):
    #     print(str(rg_start[i]) + ' ' + str(rg_end[i]) + ' ' + str(rg_slope[i]))

    wt_time = 0

    for i in range(0, priority_level):

        max_gain = -1.0
        max_class = -1

        for j in range(0, priority_level):
            if (rg_priority[j] == -1):
                gain_j = 0.0
                for k in range(0, priority_level):
                    if (rg_priority[k] == -1):
                        gain_j += PerformanceGain(rg_nbdelay[j] + wt_time, rg_num[j], rg_nbdelay[k] + wt_time, rg_num[k],
                                                 avg_processing, avg_consuming)

                if (gain_j > max_gain):
                    max_gain = gain_j
                    max_class = j
                # print(gain_j)
        # print(max_class)
        wt_time += avg_consuming * rg_num[max_class]
        rg_priority[max_class] = priority_level - i

    # print(str(len(rg_priority)))
    return rg_priority, rg_start, rg_end


def SLPriSettings(requests):  # Just SL

    priority_level = 250
    max_value = max(requests)
    min_value = min(requests)
    # print(str(max_value))
    # print(str(min_value))

    pri_range = (max_value - min_value) / (priority_level + 0.0)

    rg_start = []
    rg_end = []
    rg_slope = []
    rg_qoe = []
    rg_priority = []
    st_value = min_value

    while (st_value < max_value):
        rg_start.append(st_value)
        st_value += pri_range / 2.0
        qoe, slope = QoECurve.QoECurve(st_value)
        rg_slope.append(slope)
        rg_qoe.append(qoe)
        st_value += pri_range / 2.0
        rg_end.append(st_value)
        rg_priority.append(-1)

    # for i in range(0, priority_level):
    #     print(str(rg_start[i]) + ' ' + str(rg_end[i]) + ' ' + str(rg_slope[i]))

    for i in range(0, priority_level):

        max_slope = 100.0
        max_class = -1

        for j in range(0, len(rg_priority)):
            if ((rg_priority[j] == -1) and (rg_slope[j] <= max_slope)):
                max_slope = rg_slope[j]
                max_class = j

        rg_priority[max_class] = priority_level - i

    return rg_priority, rg_start, rg_end


def EDFPriSettings(requests):
    priority_level = 250.0
    max_value = max(requests)
    min_value = min(requests)

    pri_range = (max_value - min_value) / (priority_level + 0.0)

    rg_start = []
    rg_end = []
    rg_priority = []
    st_value = min_value

    pri_level = 0

    while (st_value < max_value):
        rg_start.append(st_value)
        st_value += pri_range
        rg_end.append(st_value)
        rg_priority.append(pri_level)
        pri_level += 1

    return rg_priority, rg_start, rg_end
