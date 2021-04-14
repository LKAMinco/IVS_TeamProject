# Name:        CalcInterface.py
# Description: IVS Project 2
# Author:      Jakub Julius Smykal
# Date:        14.4.2021

import MathLib
import re

def InputProcessing(input):
	sInput = re.split('(\+|\-|\*|\/|\!|abs|sin|cos)' ,input)
	print(sInput)
	if sInput[0] == '' and sInput[1] == '-':
		number = -1*float(sInput[2])
		sInput[1]= '0'
	elif sInput[0] == '':
		number = float(sInput[2])
	else:
		number = float(sInput[0])
	for i in range(0, len(sInput)):
		if sInput[i] == '+':
			number = MathLib.Add(float(number), float(sInput[i + 1]))
		elif sInput[i] == '-':
			number = MathLib.Sub(float(number), float(sInput[i + 1]))
		elif sInput[i] == '*':
			number = MathLib.Multiply(float(number), float(sInput[i + 1]))
		elif sInput[i] == '/':
			number = MathLib.Divide(float(number), float(sInput[i + 1]))
		elif sInput[i] == '!':
			number = MathLib.Fac(float(sInput[i-1]))
		elif sInput[i] == 'abs':
			number = MathLib.Abs(float(sInput[i + 1]))
		elif sInput[i] == 'sin':
			number = MathLib.Sin(float(sInput[i + 1]))
		elif sInput[i] == 'cos':
			number = MathLib.Cos(float(sInput[i + 1]))
	return number