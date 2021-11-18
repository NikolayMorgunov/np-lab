import numpy as np


def moving_average(a, n):
    ret = np.cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    for i in range(n):
        ret[i] /= (i + 1)
    ret[n:] /= n
    return ret
