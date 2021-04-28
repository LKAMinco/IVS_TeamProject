# Name:        MathLib.py
# Description: IVS Project 2
# Authors:     Jakub Julius Smykal
# Date:        16.4.2021

##
# @file     MathLib.py
#
# @author   Jakub Julius Smykal
#
# @brief    Basic math library for the calculator
#
# @date     16.4.2021

#!/usr/bin/python

from math import sin
from math import cos
from math import pi

##
# @brief    Addition
# 
# @param    a     first operand
# @param    b     second operand
#
# @return   Sum of a and b
def Add(a,b):
    try:
        return a+b
    except TypeError:
        raise ValueError
    
##
# @brief    Subtraction
# 
# @param    a    first operand
# @param    b    second operand
#
# @return   Difference of a and b
def Sub(a,b):
    try:
        return a-b
    except TypeError:
        raise  ValueError

##
# @brief    Multiplication
# 
# @param    a    first operand
# @param    b    second operand
#
# @return   Product of a and b
def Multiply(a,b):
    try:
        return round(a*b,17)
    except TypeError:
        raise ValueError

##
# @brief    Division
# 
# @param    a    first operand
# @param    b    second operand
#
# @return   Quotient of a and b
def Divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        raise ValueError
    except TypeError:
        raise ValueError

##
# @brief    Factorial
# 
# @param    n    non-negative integer
#
# @return   Factorial of n
def Fac(n):
    assert n >= 0
    try:
        if n == 1 or n == 0:
            return 1
        result = 1
        while n > 1:
            result = result * n
            n = n - 1
        return result
    except TypeError:
        raise ValueError
    except AssertionError:
        raise ValueError

##
# @brief    Power (b^n)
# 
# @param    b	base    
# @param    n	exponent
#
# @return   Base raised to the exponent
def Power(b,n):
    try:
        if b == 0 and n < 0:
            return 0
        return b**n
    except TypeError:
        raise ValueError
##
# @brief    Root (r^(1/i))
# 
# @param    r    radicand
# @param    i    index
#
# @return   i-th root of r
def Root(r,i):
    try:
        return round(r**(1/i),10)
    except ValueError:
        raise ValueError
    except TypeError:
        raise ValueError

##
# @brief    Convert radians to degrees
# 
# @param    a    radians to be converted
#
# @return   a represented in degrees
def Rad2Deg(a):
    try:
        return a * 180 / pi
    except TypeError:
        raise ValueError

##
# @brief    Convert degrees to radians
# 
# @param    a    degrees to be converted
#
# @return   a represented in radians
def Deg2Rad(a):
    try:
        return a * pi / 180
    except TypeError:
        raise ValueError

##
# @brief    Sine
# 
# @param    a    angle in degrees
#
# @return   Sine of a
def Sin(a):
    try:
        a = Deg2Rad(a)
        a = round(sin(a), 10)
        return a
    except TypeError:
        raise ValueError

##
# @brief    Cosine
# 
# @param    a    angle in degrees
#
# @return   Cosine of a
def Cos(a):
    try:
        a = Deg2Rad(a)
        a = round(cos(a), 10)
        return a
    except:
        raise ValueError

##
# @brief    Absolute value
# 
# @param    a    real number
#
# @return   Absolute value of a
def Abs(a):
    try:
        if a >= 0:
            return a
        else:
            return -a
    except TypeError:
        raise ValueError

##
# @brief    Engine power conversion
# 
# @param    a    value to be converted
# @param    b    power units
#
# @return   Converts Horse Power to KiloWatts, respectively
def PowerConvert(a,b):
    try:
        if b == "HP":
            return round(a / 1.34102209,4)
        elif b == "KW":
            return round(a * 1.34102209,4)
        else:
            raise ValueError
    except TypeError:
        raise ValueError

##
# @brief    Engine torque conversion
# 
# @param    a    value to be converted
# @param    b    torque units
#
# @return   Converts NewtonMeter to lbs-ft, respectively
def TorqueConvert(a,b):
    try:
        if b == "NM":
            return round(a * 0.73756214728,4)
        elif b == "lbs-ft":
            return round(a / 0.73756214728,4)
        else:
            raise ValueError
    except TypeError:
        raise ValueError

###