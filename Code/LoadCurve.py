import numpy as np

def load_curve():
    x = np.load("x_amazon.npy")
    y = np.load("y_amazon.npy")
    x = x * 1000
    # print(x)
    return x, y

def get_params():
    x, y = load_curve()
    n = np.shape(x)[0]
    slopes = []
    b = []
    

    for i in range(n):
        if i == 0:
            slopes.append(0.0)
            b.append(0.0)
        else:
            _slope = ((y[i] - y[i - 1]) + 0.0 ) / (x[i] - x[i - 1])
            _b = ((x[i]*y[i - 1] - x[i - 1]*y[i])+0.0) / (x[i] - x[i - 1])
            slopes.append(_slope)
            b.append(_b)
    
    slopes.append(0.0)
    b.append(0.0)

    np.savez("curve_params.npz", slopes=slopes, b=b)
    print(x)
    print(y)

def test_module():
    get_params()
    f = np.load("curve_params.npz")
    slopes = f['slopes']
    b = f['b']
    print(slopes)
    print(b)

test_module()