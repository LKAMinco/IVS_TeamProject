# Name:        CalcInterface.py
# Description: IVS Project 2
# Authors:      Jakub Julius Smykal, Filip Bucko
# Date:        14.4.2021

import MathLib
import re
from PyQt5 import QtWidgets
from gui import Ui_MainWindow

##
# @brief    User Input
#
# @details  This function collects user input and stores it in a string variable
#

class CalculatorWindow(QtWidgets.QMainWindow,Ui_MainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.show()

		#Create button connections for digits
		self.pushButton_zero.clicked.connect(self.digit_pressed)
		self.pushButton_one.clicked.connect(self.digit_pressed)
		self.pushButton_two.clicked.connect(self.digit_pressed)
		self.pushButton_three.clicked.connect(self.digit_pressed)
		self.pushButton_four.clicked.connect(self.digit_pressed)
		self.pushButton_five.clicked.connect(self.digit_pressed)
		self.pushButton_six.clicked.connect(self.digit_pressed)	
		self.pushButton_seven.clicked.connect(self.digit_pressed)
		self.pushButton_eight.clicked.connect(self.digit_pressed)
		self.pushButton_nine.clicked.connect(self.digit_pressed)
	
		#Create button connections for decimal point
		self.pushButton_dot.clicked.connect(self.decimal_pressed)
		
		#Create button connections for clearing display
		self.pushButton_clear.clicked.connect(self.clear_pressed)	
		self.pushButton_del.clicked.connect(self.del_pressed)
		
		#Create button connections for math operations
		self.pushButton_add.clicked.connect(self.add_pressed)
		self.pushButton_sub.clicked.connect(self.sub_pressed)
		self.pushButton_mul.clicked.connect(self.mul_pressed)
		self.pushButton_div.clicked.connect(self.div_pressed)	
		self.pushButton_pow.clicked.connect(self.pow_pressed)	
		self.pushButton_sqr.clicked.connect(self.sqr_pressed)	
		self.pushButton_result.clicked.connect(self.result_pressed)
	
		#Create button connections for advanced math operations	
		self.action_sin.triggered.connect(self.sin_pressed)
		self.action_cos.triggered.connect(self.cos_pressed)
		self.action_abs.triggered.connect(self.abs_pressed)
		self.action_fac.triggered.connect(self.fac_pressed)

	def digit_pressed(self):
		button = self.sender()
		newLabel = self.lineEdit_results.text() + button.text()
		#Verification of multiple occurence of zero at the beginning
		if len(newLabel)>1:
			if (newLabel[0]=='0') and (newLabel[1]!='.'):
				newLabel = newLabel[1:]
		self.lineEdit_results.setText(newLabel)

	def decimal_pressed(self):	
		#Verification of multiple occurence of decimal point
		newLabel = self.lineEdit_results.text()
		if (newLabel.count('.')==0):
			self.lineEdit_results.setText(newLabel + '.')
	
	def clear_pressed(self):
		self.lineEdit_results.setText('')	

	def del_pressed(self):
		newLabel = self.lineEdit_results.text()	
		self.lineEdit_results.setText(newLabel[:-1])

	def add_pressed(self):
		button = self.sender()
		newLabel = self.lineEdit_results.text() + button.text()
		self.lineEdit_results.setText(newLabel)
	
	def sub_pressed(self):
		button = self.sender()
		newLabel = self.lineEdit_results.text() + button.text()
		self.lineEdit_results.setText(newLabel)
	
	def mul_pressed(self):
		button = self.sender()
		newLabel = self.lineEdit_results.text() + '*'
		self.lineEdit_results.setText(newLabel)
	
	def div_pressed(self):
		button = self.sender()
		newLabel = self.lineEdit_results.text() + button.text()
		self.lineEdit_results.setText(newLabel)

	def pow_pressed(self):
		button = self.sender()
		newLabel = self.lineEdit_results.text() + button.text()
		self.lineEdit_results.setText(newLabel)
	
	def sqr_pressed(self):
		button = self.sender()
		newLabel = self.lineEdit_results.text() + button.text()
		self.lineEdit_results.setText(newLabel)
	
	def result_pressed(self):
		result = self.lineEdit_results.text()
		result = InputProcessing(result)
		self.lineEdit_results.setText(str(result))

	def sin_pressed(self):
		button = self.sender()
		newLabel = self.lineEdit_results.text() + 'sin'
		self.lineEdit_results.setText(newLabel)
	def cos_pressed(self):
		button = self.sender()
		newLabel = self.lineEdit_results.text() + 'cos' 
		self.lineEdit_results.setText(newLabel)
	def abs_pressed(self):
		button = self.sender()
		newLabel = self.lineEdit_results.text() + 'abs'
		self.lineEdit_results.setText(newLabel)
	def fac_pressed(self):
		button = self.sender()
		newLabel = self.lineEdit_results.text() + '!'
		self.lineEdit_results.setText(newLabel)
##
# @brief    Processing of user input
#
# @param    a input in string format
#
# @return   Calculates the result of inserted numbers,operands

def InputProcessing(input):
	#Splits the string according to the operands
	sInput = re.split('(\+|\-|\*|\/|\!|abs|sin|cos|\^|\√)' ,input)
	#This if checks if first inserted number is postive or negative
	if sInput[0] == '' and sInput[1] == '-':
		number = -1*float(sInput[2])
		sInput[1]= '0'
	#This elif checks if any function which is written in front of the number was inserted
	elif sInput[0] == '':
		number = sInput[2]
	else:
		number = float(sInput[0])
		for i in range(0, len(sInput)):
			if sInput[i] == '+':
				#Checks if next number is positiv or negative, in case of negative number it modifies the list
				if sInput[i + 1] == '':
					sInput[i + 1] = int(-1)*float(sInput[i + 3])
					sInput[i + 2] = '0' #Replacement for '-', wont affect calculations
				number = MathLib.Add(float(number), float(sInput[i + 1]))
			elif sInput[i] == '-':
				if sInput[i + 1] == '': #Look at line 113 for definition
					sInput[i + 1] = int(-1)*float(sInput[i + 3])
					sInput[i + 2] = '0'
				number = MathLib.Sub(float(number), float(sInput[i + 1]))
			elif sInput[i] == '*':
				if sInput[i + 1] == '': #Look at line 113 for definition
					sInput[i + 1] = int(-1)*float(sInput[i + 3])
					sInput[i + 2] = '0'
				number = MathLib.Multiply(float(number), float(sInput[i + 1]))
			elif sInput[i] == '/':
				if sInput[i + 1] == '': #Look at line 113 for definition
					sInput[i + 1] = int(-1)*float(sInput[i + 3])
					sInput[i + 2] = '0'
				#Division by 0 handling
				if sInput[i + 1] == '0' or sInput[i + 1] == -0:
					return 'Error'
				number = MathLib.Divide(float(number), float(sInput[i + 1]))
			elif sInput[i] == '!':
				# Checks if number is positive or negative
				if number >= 0:
					number = MathLib.Fac(float(number))
				else:
					number = -1 * MathLib.Fac(-1*float(number))
			elif sInput[i] == 'abs':
				if sInput[i + 1] == '': #Look at line 113 for definition
					sInput[i + 1] = int(-1)*float(sInput[i + 3])
					sInput[i + 2] = '0'
				number = MathLib.Abs(float(sInput[i + 1]))
			elif sInput[i] == 'sin':
				if sInput[i + 1] == '': #Look at line 113 for definition
					sInput[i + 1] = int(-1)*float(sInput[i + 3])
					sInput[i + 2] = '0'
				number = MathLib.Sin(float(sInput[i + 1]))
			elif sInput[i] == 'cos':
				if sInput[i + 1] == '': #Look at line 113 for definition
					sInput[i + 1] = int(-1)*float(sInput[i + 3])
					sInput[i + 2] = '0'
				number = MathLib.Cos(float(sInput[i + 1]))
			elif sInput[i] == '^':
				if sInput[i + 1] == '': #Look at line 113 for definition
					sInput[i + 1] = int(-1) * float(sInput[i + 3])
					sInput[i + 2] = '0'
				number = MathLib.Power(float(number), float(sInput[i + 1]))
			elif sInput[i] == '√':
				#If number is negative it returns error
				if sInput[i + 1] == '':
					return 'Error'
				number = MathLib.Root(float(sInput[i + 1]),float(sInput[i - 1]))
	return number
