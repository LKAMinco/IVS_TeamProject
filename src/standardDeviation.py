#!/usr/bin/python3.8

from MathLib import *

def variance(values):
    N = len(values)
    s_mean = 0
    s_seq = 0
    for val in values:
        s_mean = Add(s_mean, val)
        s_seq = Add(s_seq, Power(val, 2))
    mean = Divide(s_mean, N)
    return Divide(Sub(s_seq, Multiply(N, Power(mean, 2))), N-1)

def standardDeviation(values):
    return Root(variance(values), 2)
