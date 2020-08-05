import numpy as np


def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.2, 0.5])
    b = -0.7
    tmp = np.sum(w*x) + b
    return 0 if tmp <= 0 else 1


def NAND(x1, x2):
    return 0 if AND(x1, x2) == 1 else 1


def OR(x1, x2):


print(NAND(1, 2))
