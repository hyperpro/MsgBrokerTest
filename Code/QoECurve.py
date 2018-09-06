#!/usr/bin/env python
import math
import numpy as np
#Input: latency
#Output: QoE and Slope

x = [  940.,  1360.,  2180.,  3360.,  4260.,  5160.,  6400.,  8000.,  9960., 12860., 20520., 30520.]
y = [4.62, 4.6,  4.58, 4.33, 3.99, 3.73, 3.06, 2.64, 2.42, 2.24, 1.85, 1.45]
slopes = [ 0.00000000e+00, -4.76190476e-05, -2.43902439e-05, -2.11864407e-04,
 -3.77777778e-04, -2.88888889e-04, -5.40322581e-04, -2.62500000e-04,
 -1.12244898e-04, -6.20689655e-05, -5.09138381e-05, -4.00000000e-05,
  0.00000000e+00]
b = [0.,         4.6647619,  4.63317073, 5.04186441, 5.59933333, 5.22066667,
 6.51806452, 4.74,       3.53795918, 3.0382069,  2.89475196, 2.6708,
 0.        ]



def load_curve():
    x = np.load("x_amazon.npy")
    y = np.load("y_amazon.npy")
    x = x * 1000
    # print(x)
    return x, y

def QoECurve(e2e_latency):
    
    Slope = 0  # the slope on the curve when e2e latency is e2e_latency
    QoE = 0  # the QoE when e2e latency is e2e_latency


    # if (e2e_latency < 1000.0):

    #     QoE = -0.0005 * e2e_latency + 1.0
    #     Slope = -0.0005

    # elif (e2e_latency > 1000.0 and e2e_latency < 1500):

    #     QoE = -0.0002999999999998 * e2e_latency + 1.249999999998
    #     Slope = -0.0002999999999998

    # elif (e2e_latency <= 2400 and e2e_latency >= 1500):

    #     QoE = -0.0008666666666667 * e2e_latency + 2.1
    #     Slope = -0.0008666666666667

    # else:

    #     QoE = -0.00000416666666666667 * e2e_latency + 0.03
    #     Slope = -0.00000416666666666667

    # x, y = load_curve()
    # n = 12
    # f = np.load("curve_params.npz")
    # slopes = f['slopes']
    # b = f['b']
    n = 12
    zone_flag = 0
    for i in range(n):
        if e2e_latency > x[i]: zone_flag = zone_flag + 1
        else: break
    if zone_flag == 0:
        QoE = y[0]
        Slope = 0
    elif zone_flag == n:
        QoE = y[n-1]
        Slope = 0
    else:
        Slope = slopes[zone_flag]
        QoE = Slope * e2e_latency + b[zone_flag]
    # print(zone_flag, e2e_latency, Slope)
    
    return QoE, Slope
