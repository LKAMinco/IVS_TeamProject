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
    return a+b
    
##
# @brief    Subtraction
# 
# @param    a    first operand
# @param    b    second operand
#
# @return   Difference of a and b
def Sub(a,b):
    return a-b

##
# @brief    Multiplication
# 
# @param    a    first operand
# @param    b    second operand
#
# @return   Product of a and b
def Multiply(a,b):
    return a*b

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
    except:
        print("Error: Division by zero")
        return None

##
# @brief    Factorial
# 
# @param    n    non-negative integer
#
# @return   Factorial of n
def Fac(n):
    if n == 1:
        return 1
    return n*Fac(n-1)

##
# @brief    Power (b^n)
# 
# @param    b	base    
# @param    n	exponent
#
# @return   Base raised to the exponent
def Power(b,n):
    return b**n

##
# @brief    Root (r^(1/i))
# 
# @param    r    radicand
# @param    i    index
#
# @return   i-th root of r
def Root(r,i):
    try:
        return r**(1/i)
    except:
        print("Error: Invalid input")
        return None

##
# @brief    Convert radians to degrees
# 
# @param    a    radians to be converted
#
# @return   a represented in degrees
def Rad2Deg(a):
    return a * 180 / pi

##
# @brief    Convert degrees to radians
# 
# @param    a    degrees to be converted
#
# @return   a represented in radians
def Deg2Rad(a):
    return a * pi / 180

##
# @brief    Sine
# 
# @param    a    angle in radians 
#
# @return   Sine of a
def Sin(a):
    a = Deg2Rad(a)
    a = round(sin(a), 10)
    return a

##
# @brief    Cosine
# 
# @param    a    angle in radians 
#
# @return   Cosine of a
def Cos(a):
    a = Deg2Rad(a)
    a = round(cos(a), 10)
    return a

##
# @brief    Absolute value
# 
# @param    a    real number
#
# @return   Absolute value of a
def Abs(a):
    if a >= 0:
        return a
    else:
        return -a

##
# @brief    Engine power conversion
# 
# @param    a    value to be converted
# @param    b    power units
#
# @return   Converts Horse Power to KiloWatts, respectively
def PowerConvert(a,b):
    if b == "HP":
        return a / 1.34102209
    elif b == "KW":
        return a * 1.34102209
    else:
        print("Error: Invalid units")
        return None

##
# @brief    Engine torque conversion
# 
# @param    a    value to be converted
# @param    b    torque units
#
# @return   Converts NewtonMeter to lbs-ft, respectively
def TorqueConvert(a,b):
    if b == "NM":
        return a * 0.73756214728
    elif b == "lbs-ft":
        return a / 0.73756214728
    else:
        print("Error: Invalid units")
        return None
