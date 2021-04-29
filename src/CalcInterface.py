# Authors:		Jakub Julius Smykal, Filip Bucko
# Date:			14.4.2021

##
# @file     CalcInterface.py
#
# @author   Jakub Julius Smykal, Filip Bucko
#
# @brief    Function to gather and process input, joins GUI with math library
#
# @date     14.4.2021

import MathLib
import webbrowser
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

		#Create button connections for convertor 	
		self.action_hp2kw.triggered.connect(self.hp2kw_pressed)
		self.action_kw2hp.triggered.connect(self.kw2hp_pressed)
		self.action_rad2deg.triggered.connect(self.rad2deg_pressed)
		self.action_deg2rad.triggered.connect(self.deg2rad_pressed)
		self.action_nm2lbsft.triggered.connect(self.nm2lbsft_pressed)
		self.action_lbsft2nm.triggered.connect(self.lbsft2nm_pressed)

		#Create button connections for help	
		self.actionDocumentation.triggered.connect(self.manual_pressed)

	def digit_pressed(self):
		operations = ['*','/','+','-','^','√']
		button = self.sender()
		newLabel = self.lineEdit_results.text()
		
		if(ErrorCheck(self,newLabel)):
			return
		
		#Verification of multiple occurence of zero at the beginning
		if(not newLabel):
			self.lineEdit_results.setText(newLabel+button.text())
		elif (button.text()=='0'):
			if (len(newLabel) > 1):
				if(newLabel[-1] == '0') and (newLabel[-2] in operations):
					return
			if (len(newLabel) == 1):
				if(newLabel[0] == '0'):
					return
			newLabel = newLabel + button.text()
			self.lineEdit_results.setText(newLabel)
		else:
			self.lineEdit_results.setText(newLabel+button.text())

	def decimal_pressed(self):	
		#Verification of multiple occurence of decimal point
		newLabel = self.lineEdit_results.text()
		
		if(newLabel):
			numbers = re.split('(\+|\-|\*|\/|\!|abs|sin|cos|\^|\√)' ,newLabel)
			if (numbers[-1].count('.')==0) and (newLabel[-1].isdigit()):
				self.lineEdit_results.setText(newLabel + '.')
	
	def clear_pressed(self):
		self.lineEdit_results.setText('')	
		self.label_results.setText('')	

	def del_pressed(self):
		newLabel = self.lineEdit_results.text()	
		self.label_results.setText('')	
		self.lineEdit_results.setText(newLabel[:-1])

	def add_pressed(self):
		if(self.label_results.text()):
			self.label_results.setText('')
		button = self.sender()
		newLabel = self.lineEdit_results.text()
		
		if(ErrorCheck(self,newLabel)):
			return
		
		if newLabel:
			units = RemoveUnits(newLabel)
			if (units != "present"):
				newLabel = units
			operations = ['*','/','+','-','^','√']
			if newLabel[-1] not in operations:
				newLabel += button.text()
				self.lineEdit_results.setText(newLabel)
	
	def sub_pressed(self):
		if(self.label_results.text()):
			self.label_results.setText('')
		button = self.sender()
		newLabel = self.lineEdit_results.text()
		
		if(ErrorCheck(self,newLabel)):
			return
		
		if newLabel:
			units = RemoveUnits(newLabel)
			if (units != "present"):
				newLabel = units
			if len(newLabel)>1:
				operations = ['*','/','+','-','^','√']
				if not (newLabel[-1] == '-' and (newLabel[-2] in operations)):
					newLabel += button.text()
					self.lineEdit_results.setText(newLabel)
			elif len(newLabel)==1:
				newLabel += button.text()
				if newLabel[0] != '-':
					self.lineEdit_results.setText(newLabel)
		else:
				newLabel += button.text()
				self.lineEdit_results.setText(newLabel)
	
	def mul_pressed(self):
		if(self.label_results.text()):
			self.label_results.setText('')
		button = self.sender()
		newLabel = self.lineEdit_results.text()
		
		if(ErrorCheck(self,newLabel)):
			return
		
		if newLabel:
			units = RemoveUnits(newLabel)
			if (units != "present"):
				newLabel = units
			operations = ['*','/','+','-','^','√']
			if newLabel[-1] not in operations:
				newLabel += '*'
				self.lineEdit_results.setText(newLabel)
	
	def div_pressed(self):
		if(self.label_results.text()):
			self.label_results.setText('')
		button = self.sender()
		newLabel = self.lineEdit_results.text()
		
		if(ErrorCheck(self,newLabel)):
			return
	 		 
		if newLabel:
			units = RemoveUnits(newLabel)
			if (units != "present"):
				newLabel = units
			operations = ['*','/','+','-','^','√']
			if newLabel[-1] not in operations:
				newLabel += button.text()
				self.lineEdit_results.setText(newLabel)

	def pow_pressed(self):
		if(self.label_results.text()):
			self.label_results.setText('')
		button = self.sender()
		newLabel = self.lineEdit_results.text()
		
		if(ErrorCheck(self,newLabel)):
			return
		
		if newLabel:
			units = RemoveUnits(newLabel)
			if (units != "present"):
				newLabel = units
			operations = ['*','/','+','-','^','√']
			if newLabel[-1] not in operations:
				newLabel += button.text()
				self.lineEdit_results.setText(newLabel)
	
	def sqr_pressed(self):
		if(self.label_results.text()):
			self.label_results.setText('')
		button = self.sender()
		newLabel = self.lineEdit_results.text()
		
		if(ErrorCheck(self,newLabel)):
			return
		
		if newLabel:
			units = RemoveUnits(newLabel)
			if (units != "present"):
				newLabel = units
			operations = ['*','/','+','-','^']
			if newLabel[-1] not in operations:
				newLabel += button.text()
				self.lineEdit_results.setText(newLabel)
	
	def result_pressed(self):
		result = self.lineEdit_results.text()
		self.label_results.setText(result)
		result = InputProcessing(result)
		self.lineEdit_results.setText(str(result))

	def sin_pressed(self):
		button = self.sender()
		newLabel = self.lineEdit_results.text()
		
		if(ErrorCheck(self,newLabel)):
			return
		
		if newLabel:
			units = RemoveUnits(newLabel)
			if (units != "present"):
				newLabel = units
		newLabel = newLabel + 'sin'
		self.lineEdit_results.setText(newLabel)
	
	def cos_pressed(self):
		button = self.sender()
		newLabel = self.lineEdit_results.text()
		
		if(ErrorCheck(self,newLabel)):
			return

		if newLabel:
			units = RemoveUnits(newLabel)
			if (units != "present"):
				newLabel = units
		newLabel = newLabel + 'cos'
		self.lineEdit_results.setText(newLabel)
	
	def abs_pressed(self):
		button = self.sender()
		newLabel = self.lineEdit_results.text()
		
		if(ErrorCheck(self,newLabel)):
			return
		
		if newLabel:
			units = RemoveUnits(newLabel)
			if (units != "present"):
				newLabel = units
		newLabel = newLabel + 'abs'
		self.lineEdit_results.setText(newLabel)
	
	def fac_pressed(self):
		button = self.sender()
		newLabel = self.lineEdit_results.text()
		
		if(ErrorCheck(self,newLabel)):
			return
		
		if newLabel:
			units = RemoveUnits(newLabel)
			if (units != "present"):
				newLabel = units
			operations = ['*','/','+','-','^','√']
			if newLabel[-1] not in operations:
				newLabel += '!' 
				self.lineEdit_results.setText(newLabel)

	#Convertor
	def hp2kw_pressed(self):
		newLabel = self.lineEdit_results.text()
		if(ErrorCheck(self,newLabel)):
			return
		if newLabel:
			try:
				newLabel = eval(newLabel)
				converted = MathLib.PowerConvert(float(newLabel),"HP")
				self.label_results.setText(self.lineEdit_results.text()+ " HP")
				self.lineEdit_results.setText(str(converted) + " kW")
			except SyntaxError:	
				self.lineEdit_results.setText("Incorrect format")
	def kw2hp_pressed(self):
		newLabel = self.lineEdit_results.text()
		if(ErrorCheck(self,newLabel)):
			return
		if newLabel:
			try:
				newLabel = eval(newLabel)
				converted = MathLib.PowerConvert(float(newLabel),"KW")
				self.label_results.setText(self.lineEdit_results.text()+ " kW")
				self.lineEdit_results.setText(str(converted) + " HP")
			except SyntaxError:	
				self.lineEdit_results.setText("Incorrect format")

	def rad2deg_pressed(self):
		newLabel = self.lineEdit_results.text()
		if(ErrorCheck(self,newLabel)):
			return
		if newLabel:
			try:
				newLabel = eval(newLabel)
				converted = MathLib.Rad2Deg(float(newLabel))
				self.label_results.setText(self.lineEdit_results.text()+ " rad")
				self.lineEdit_results.setText(str(converted) + "°")
			except SyntaxError:	
				self.lineEdit_results.setText("Incorrect format")

	def deg2rad_pressed(self):
		newLabel = self.lineEdit_results.text()
		if(ErrorCheck(self,newLabel)):
			return
		if newLabel:
			try:
				newLabel = eval(newLabel)
				converted = MathLib.Deg2Rad(float(newLabel))
				self.label_results.setText(self.lineEdit_results.text()+ "°")
				self.lineEdit_results.setText(str(converted) + " rad")
			except SyntaxError:	
				self.lineEdit_results.setText("Incorrect format")
	
	def nm2lbsft_pressed(self):
		newLabel = self.lineEdit_results.text()
		if(ErrorCheck(self,newLabel)):
			return
		if newLabel:
			try:
				newLabel = eval(newLabel)
				converted = MathLib.TorqueConvert(float(newLabel),"NM")
				self.label_results.setText(self.lineEdit_results.text()+ " NM")
				self.lineEdit_results.setText(str(converted) + " lbs·ft")
			except SyntaxError:	
				self.lineEdit_results.setText("Incorrect format")
	
	def lbsft2nm_pressed(self):
		newLabel = self.lineEdit_results.text()
		if(ErrorCheck(self,newLabel)):
			return
		if newLabel:
			try:
				newLabel = eval(newLabel)
				converted = MathLib.TorqueConvert(float(newLabel),"lbs-ft")
				self.label_results.setText(self.lineEdit_results.text()+ " lbs·ft")
				self.lineEdit_results.setText(str(converted) + " NM")
			except SyntaxError:	
				self.lineEdit_results.setText("Incorrect format")

	def manual_pressed(self):
		path = '../dokumentace.pdf'
		webbrowser.open_new(path)



##
# @brief		 Checks if an error occurred on display.
#				 If an error occurred function clears the screen.
# @param display Input from calculator display
#
# @return 		 Returns 1 when an error occurred and display was cleared,
#				 else 0.
def ErrorCheck(out,display):
	errors = ['E','I']
	if (display) and (display[0] in errors):
		CalculatorWindow.clear_pressed(out)
		return 1
	return 0	


##
# @brief		Removes units from number
#
# @param num	String containing digits will be adjusted
#				by tearing off the unitsin string format
#
# @return   	Returns string containing only numbers
def RemoveUnits(num):
	operations = ['*','/','+','-','^','√','!','cos','sin','abs']
	##Variable indicates whether the operation is present in expression from input 
	present = 0
	for i in operations:
		if i in num:
			present = 1
			return "present"
	if (not present) and num[0].isdigit() :	
		dot_index = num.find('.')
		if dot_index != -1:
			num = num.replace('.','0',1)
		if not (num.isdigit()):
			while not (num.isdigit()):
				num = num[:-1]
			if dot_index != -1:
				num = num[0:dot_index]+'.'+num[dot_index+1:]
			return num
		else:
			if dot_index != -1:
				num = num[0:dot_index]+'.'+num[dot_index+1:]
			return num


##
# @brief		Checks user input for invalid chars and its size
#
# @param input	part of input in string format
#
# @param min	int to check min size of number
#
# @param max	int to check max size of number
#
# @param checkChar option to look for invalid chars in string
#
# @param checkSize option to check size of number
#
# @return   	Returns false if there is something wrong with input

def CheckInput(input, min, max, checkChar, chechSize):
	if checkChar == 1:
		if re.search('[a-zA-Z]', input):
			return False
	if chechSize == 1:
		if float(input) > max:
			return False
		if float(input) < min:
			return False
	return True

##
# @brief		Processing of user input
#
# @param input	An input in string format
#
# @return   	Calculates the result of inserted numbers,operands

def InputProcessing(input):
	#Splits the string according to the operands
	sInput = re.split('(\+|\-|\*|\/|\!|abs|sin|cos|\^|\√)' ,input)
	if len(sInput) == 1:
		return input
	#This if checks if first inserted number is postive or negative
	if sInput[0] == '' and sInput[1] == '-':
		if CheckInput(sInput[2], -10, 10,1,0) == False:
			return 'Error'
		number = -1*float(sInput[2])
		sInput[1]= '0'
	#This elif checks if any function which is written in front of the number was inserted
	elif sInput[0] == '':
		number = sInput[2]
	else:
		number = float(sInput[0])
	#Checks if there is a number after operand
	if sInput[len(sInput)-1] == '' and sInput[len(sInput)-2] != '!' :
		return 'Error'
	if CheckInput(number, -1000000, 1000000, 0, 1) == False:
		return 'Error'
	for i in range(0, len(sInput)):
		if sInput[i] == '+':
			#Checks if next number is positiv or negative, in case of negative number it modifies the list
			if sInput[i + 1] == '':
				sInput[i + 1] = int(-1)*float(sInput[i + 3])
				sInput[i + 2] = '0' #Replacement for '-', wont affect calculations
			if CheckInput(sInput[i + 1], -1000000, 1000000, 0, 1) == False:
				return 'Error'
			number = MathLib.Add(float(number), float(sInput[i + 1]))
		elif sInput[i] == '-':
			if sInput[i + 1] == '': #Look at line 113 for definition
				sInput[i + 1] = int(-1)*float(sInput[i + 3])
				sInput[i + 2] = '0'
			if CheckInput(sInput[i + 1], -1000000, 1000000, 0, 1) == False:
				return 'Error'
			number = MathLib.Sub(float(number), float(sInput[i + 1]))
		elif sInput[i] == '*':
			if sInput[i + 1] == '': #Look at line 113 for definition
				sInput[i + 1] = int(-1)*float(sInput[i + 3])
				sInput[i + 2] = '0'
			if CheckInput(sInput[i + 1], -1000000, 1000000, 0, 1) == False:
				return 'Error'
			number = MathLib.Multiply(float(number), float(sInput[i + 1]))
		elif sInput[i] == '/':
			if sInput[i + 1] == '': #Look at line 113 for definition
				sInput[i + 1] = int(-1)*float(sInput[i + 3])
				sInput[i + 2] = '0'
			#Division by 0 handling
			if sInput[i + 1] == '0' or sInput[i + 1] == -0:
				return 'Error'
			if CheckInput(sInput[i + 1], -1000000, 1000000, 0, 1) == False:
				return 'Error'
			number = MathLib.Divide(float(number), float(sInput[i + 1]))
		elif sInput[i] == '!':
			# Checks if number is positive or negative
			if number < 0 or not float(number).is_integer() or number > 50:
				return 'Error'
			number = MathLib.Fac(float(number))
		elif sInput[i] == 'abs':
			if sInput[i + 1] == '': #Look at line 113 for definition
				sInput[i + 1] = int(-1)*float(sInput[i + 3])
				sInput[i + 2] = '0'
			if CheckInput(sInput[i + 1], -1000000, 1000000, 0, 1) == False:
				return 'Error'
			number = MathLib.Abs(float(sInput[i + 1]))
		elif sInput[i] == 'sin':
			if sInput[i + 1] == '': #Look at line 113 for definition
				sInput[i + 1] = int(-1)*float(sInput[i + 3])
				sInput[i + 2] = '0'
			if CheckInput(sInput[i + 1], -10000, 10000, 0, 1) == False:
				return 'Error'
			number = MathLib.Sin(float(sInput[i + 1]))
		elif sInput[i] == 'cos':
			if sInput[i + 1] == '': #Look at line 113 for definition
				sInput[i + 1] = int(-1)*float(sInput[i + 3])
				sInput[i + 2] = '0'
				if CheckInput(sInput[i + 1], -10000, 10000, 0, 1) == False:
					return 'Error'
			number = MathLib.Cos(float(sInput[i + 1]))
		elif sInput[i] == '^':
			if sInput[i + 1] == '': #Look at line 113 for definition
				sInput[i + 1] = int(-1) * float(sInput[i + 3])
				sInput[i + 2] = '0'
			if CheckInput(sInput[i + 1], -20, 20,0,1) == False:
				return 'Error: Invalid Exponent'
			number = MathLib.Power(float(number), float(sInput[i + 1]))
		elif sInput[i] == '√':
			#If number is negative it returns error
			if sInput[i + 1] == '':
				return 'Error'
			if CheckInput(sInput[i + 1], 0, 1000000, 0, 1) == False:
				return 'Error'
			number = MathLib.Root(float(sInput[i + 1]),float(sInput[i - 1]))
	if float(number).is_integer():
		number = int(number)
	return number
