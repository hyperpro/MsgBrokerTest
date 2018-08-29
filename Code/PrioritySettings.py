#!/usr/bin/env python

import sys
import math
import QoECurve

def OurPriSettings(requests):

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
        st_value += pri_range/2.0
        qoe, slope = QoECurve.QoECurve(st_value)
        rg_slope.append(slope)
        rg_qoe.append(qoe)
        st_value += pri_range/2.0
        rg_end.append(st_value)
        rg_priority.append(-1)

    # for i in range(0, priority_level):
    #     print(str(rg_start[i]) + ' ' + str(rg_end[i]) + ' ' + str(rg_slope[i]))

    for i in range(0, priority_level):

        max_qoe = -1.0
        max_slope = 100.0
        max_class = -1
        for j in range(0, len(rg_priority)):
            if ( (rg_priority[j] == -1) and (rg_slope[j] <= max_slope)):
                if (rg_slope[j] >= max_slope - 0.00002):
                    if (rg_qoe[j] > max_qoe):
                        max_qoe = rg_qoe[j]
                        max_slope = rg_slope[j]
                        max_class = j
                else:
                    max_qoe = rg_qoe[j]
                    max_slope = rg_slope[j]
                    max_class = j

        rg_priority[max_class] = priority_level - i

    return rg_priority, rg_start, rg_end

def EDFPriSeetings(requests):

    priority_level = 250.0
    max_value = max(requests)
    min_value = min(requests)

    pri_range = (max_value - min_value) / priority_level

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
