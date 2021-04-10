#!/usr/bin/python3.8

from MathLib import *
import sys
import re
from statistics import stdev

## 
# @brief    Calculate variance from given data
# 
# @param    values  list of numbers separated with whitespace
# @return   variance of numbers
def variance(values):
    N = len(values)
    s_mean = 0
    s_seq = 0
    for val in values:
        s_mean = Add(s_mean, val)
        s_seq = Add(s_seq, Power(val, 2))
    mean = Divide(s_mean, N)
    return Divide(Sub(s_seq, Multiply(N, Power(mean, 2))), N-1)

##
# @brief    Calculate standard deviation from given data
#
# @param    values  list of numbers separated with whitespace
# @return   standard deviation of numbers
def standardDeviation(values):
    return Root(variance(values), 2)


# Example of reading comma separated values from stdin
values = []
for line in sys.stdin:
    data = line.strip().replace('\n', ',')
    # supported separation: (, ) - comma+space
    #                       (,) - comma only
    #                       ( ) - space only
    values += [float(x) for x in re.split(', |,| ', data)]

#print(values)
# Example usage: ./standardDeviation.py < data.txt
print(standardDeviation(values))
print(stdev(values))
