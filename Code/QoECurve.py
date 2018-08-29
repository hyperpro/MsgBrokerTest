#!/usr/bin/env python
import math

#Input: latency
#Output: QoE and Slope

def QoECurve(e2e_latency):

    Slope = 0  # the slope on the curve when e2e latency is e2e_latency
    QoE = 0  # the QoE when e2e latency is e2e_latency

    '''
    Your QoE Curve goes here
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
    QoE Curve ends Here
    '''

    return QoE, Slope
