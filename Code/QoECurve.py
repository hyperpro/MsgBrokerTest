#!/usr/bin/env python
import math
import numpy as np
#Input: latency
#Output: QoE and Slope

def load_curve():
    x = np.load("x_amazon.npy")
    y = np.load("y_amazon.npy")
    x = x * 1000
    print x
    return x, y

def QoECurve(e2e_latency):

    Slope = 0  # the slope on the curve when e2e latency is e2e_latency
    QoE = 0  # the QoE when e2e latency is e2e_latency

    '''
    Your QoE Curve goes here
    '''

    '''
    if (e2e_latency < 1000.0):

        QoE = -0.0005 * e2e_latency + 1.0
        Slope = -0.0005

    elif (e2e_latency > 1000.0 and e2e_latency < 1500):

        QoE = -0.0002999999999998 * e2e_latency + 1.249999999998
        Slope = -0.0002999999999998

    elif (e2e_latency <= 2400 and e2e_latency >= 1500):

        QoE = -0.0008666666666667 * e2e_latency + 2.1
        Slope = -0.0008666666666667

    else:

        QoE = -0.00000416666666666667 * e2e_latency + 0.03
        Slope = -0.00000416666666666667
    '''
    '''
    QoE Curve ends Here
    '''
    x, y = load_curve()
    n = np.shape(x)[0]
    zone_flag = 0
    for i in range(n):
        if e2e_latency > x[i]: zone_flag = zone_flag + 1
        else: break
    if zone_flag == 0:
        QoE = x[0]
        Slope = 0
    elif zone_flag == n:
        QoE = x[n-1]
        Slope = 0
    else:
        Slope = (y[zone_flag] - y[zone_flag - 1]) / (x[zone_flag] - x[zone_flag - 1])
        b = (x[zone_flag]*y[zone_flag - 1] - x[zone_flag - 1]*y[zone_flag]) / (x[zone_flag] - x[zone_flag - 1])
        QoE = Slope * e2e_latency + b
    return QoE, Slope
