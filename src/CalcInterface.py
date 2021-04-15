# Name:        CalcInterface.py
# Description: IVS Project 2
# Author:      Jakub Julius Smykal
# Date:        14.4.2021

import MathLib
import re
from PyQt5 import QtWidgets
from gui import Ui_MainWindow

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
		self.pushButton_result.clicked.connect(self.result_pressed)

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

	def result_pressed(self):
		result = self.lineEdit_results.text()
		result = InputProcessing(result)
		self.lineEdit_results.setText(str(result))

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
