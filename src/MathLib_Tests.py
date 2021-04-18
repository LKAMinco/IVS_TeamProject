# Name:        MathLib_Tests.py
# Description: IVS Project 2
# Author:      Filip Bucko
# Date:        5.4.2021

import unittest
import MathLib

# Test case to verify the correctness of the addition
# function: Add(a,b)
class AdditionTest(unittest.TestCase):

	def testZeroDivisionErrors(self):
		with self.assertRaises(ZeroDivisionError):
			MathLib.Add(1/0,1/0)	
		with self.assertRaises(ZeroDivisionError):
			MathLib.Add(1/0,0)
		with self.assertRaises(ZeroDivisionError):
			MathLib.Add(0,1/0)

	def testFloatAddition(self):
		self.assertEqual(MathLib.Add(0.1,0),0.1)
		self.assertEqual(MathLib.Add(0.1,0.1),0.2)
		self.assertEqual(MathLib.Add(0.111,0.111),0.222)
		self.assertEqual(MathLib.Add(1/3,1/3),2/3)
		self.assertEqual(MathLib.Add(2/3,-1/3),1/3)
		self.assertEqual(MathLib.Add(-2/3,-1/3),-1)
	
	def testPositiveNums(self):
		self.assertEqual(MathLib.Add(0,0),0)
		self.assertEqual(MathLib.Add(0,1),1)
		self.assertEqual(MathLib.Add(1,0),1)
		self.assertEqual(MathLib.Add(100,50),150)
		self.assertEqual(MathLib.Add(999,1),1000)
		self.assertEqual(MathLib.Add(1,999),1000)

	def testNegativeNums(self):
		self.assertEqual(MathLib.Add(-1,0),-1)
		self.assertEqual(MathLib.Add(0,-1),-1)
		self.assertEqual(MathLib.Add(-10,-90),-100)
		self.assertEqual(MathLib.Add(-90,-10),-100)
		self.assertEqual(MathLib.Add(-999,-1),-1000)
		self.assertEqual(MathLib.Add(-1,-999),-1000)

	def testPositiveNegativeNums(self):
		self.assertEqual(MathLib.Add(-1,1),0)
		self.assertEqual(MathLib.Add(1,-1),0)
		self.assertEqual(MathLib.Add(100,-90),10)
		self.assertEqual(MathLib.Add(-90,100),10)
		self.assertEqual(MathLib.Add(90,-100),-10)
		self.assertEqual(MathLib.Add(-100,90),-10)
	

# Test case to verify the correctness of the subtraction
# function: Sub(a,b)
class SubtractionTest(unittest.TestCase):
	
	def testZeroDivisionErrors(self):
		with self.assertRaises(ZeroDivisionError):
			MathLib.Sub(1/0,1/0)	
		with self.assertRaises(ZeroDivisionError):
			MathLib.Sub(1/0,0)
		with self.assertRaises(ZeroDivisionError):
			MathLib.Sub(0,1/0)
	
	def testFloatSubtraction(self):
		self.assertEqual(MathLib.Sub(0.1,0),0.1)
		self.assertEqual(MathLib.Sub(0.1,0.1),0)
		self.assertEqual(MathLib.Sub(0.111,0.111),0)
		self.assertEqual(MathLib.Sub(1/3,1/3),0)
		self.assertEqual(MathLib.Sub(2/3,-1/3),1)
		self.assertEqual(MathLib.Sub(-2/3,-1/3),-1/3)
	
	def testPositiveNums(self):
		self.assertEqual(MathLib.Sub(0,0),0)
		self.assertEqual(MathLib.Sub(0,1),-1)
		self.assertEqual(MathLib.Sub(1,0),1)
		self.assertEqual(MathLib.Sub(100,50),50)
		self.assertEqual(MathLib.Sub(999,1),998)
		self.assertEqual(MathLib.Sub(1,999),-998)

	def testNegativeNums(self):
		self.assertEqual(MathLib.Sub(-1,0),-1)
		self.assertEqual(MathLib.Sub(0,-1),1)
		self.assertEqual(MathLib.Sub(-10,-90),80)
		self.assertEqual(MathLib.Sub(-90,-10),-80)
		self.assertEqual(MathLib.Sub(-999,-1),-998)
		self.assertEqual(MathLib.Sub(-1,-999),998)

	def testPositiveNegativeNums(self):
		self.assertEqual(MathLib.Sub(-1,1),-2)
		self.assertEqual(MathLib.Sub(1,-1),2)
		self.assertEqual(MathLib.Sub(100,-90),190)
		self.assertEqual(MathLib.Sub(-90,100),-190)
		self.assertEqual(MathLib.Sub(90,-100),190)
		self.assertEqual(MathLib.Sub(-100,90),-190)
	
# Test case to verify the correctness of the multiplication
# function: Multiply(a,b)
class MultiplicationTest(unittest.TestCase):
	
	def testZeroDivisionErrors(self):
		with self.assertRaises(ZeroDivisionError):
			MathLib.Multiply(1/0,1/0)	
		with self.assertRaises(ZeroDivisionError):
			MathLib.Multiply(1/0,0)
		with self.assertRaises(ZeroDivisionError):
			MathLib.Multiply(0,1/0)
	
	def testFloatMultiplication(self):
		self.assertEqual(MathLib.Multiply(0.1,0),0)
		self.assertEqual(MathLib.Multiply(0.1,0.1),0.01)
		self.assertEqual(MathLib.Multiply(0.5,0.5),0.25)
		self.assertEqual(MathLib.Multiply(1/3,1/3),1/9)
		self.assertEqual(MathLib.Multiply(2/3,-1/3),-2/9)
		self.assertEqual(MathLib.Multiply(-2/3,-1/3),2/9)
	
	def testPositiveNums(self):
		self.assertEqual(MathLib.Multiply(0,0),0)
		self.assertEqual(MathLib.Multiply(0,1),0)
		self.assertEqual(MathLib.Multiply(1,0),0)
		self.assertEqual(MathLib.Multiply(100,50),5000)
		self.assertEqual(MathLib.Multiply(999,1),999)
		self.assertEqual(MathLib.Multiply(1,999),999)

	def testNegativeNums(self):
		self.assertEqual(MathLib.Multiply(-1,0),0)
		self.assertEqual(MathLib.Multiply(0,-1),0)
		self.assertEqual(MathLib.Multiply(-10,-90),900)
		self.assertEqual(MathLib.Multiply(-90,-10),900)
		self.assertEqual(MathLib.Multiply(-999,-1),999)
		self.assertEqual(MathLib.Multiply(-1,-999),999)

	def testPositiveNegativeNums(self):
		self.assertEqual(MathLib.Multiply(-1,1),-1)
		self.assertEqual(MathLib.Multiply(1,-1),-1)
		self.assertEqual(MathLib.Multiply(100,-90),-9000)
		self.assertEqual(MathLib.Multiply(-90,100),-9000)
		self.assertEqual(MathLib.Multiply(90,-100),-9000)
		self.assertEqual(MathLib.Multiply(-100,90),-9000)


# Test case to verify the correctness of the division
# function: Divide(a,b)
class DivisionTest(unittest.TestCase):
	
	def testZeroDivisionErrors(self):
		with self.assertRaises(ZeroDivisionError):
			MathLib.Divide(1/0,1/0)	
		with self.assertRaises(ZeroDivisionError):
			MathLib.Divide(1/0,0)
		with self.assertRaises(ZeroDivisionError):
			MathLib.Divide(0,1/0)
	
	def testFloatDivision(self):
		self.assertEqual(MathLib.Divide(0.1,0.01),10)
		self.assertEqual(MathLib.Divide(0.1,0.1),1)
		self.assertEqual(MathLib.Divide(0.5,0.25),2)
		self.assertEqual(MathLib.Divide(1/3,1/3),1)
		self.assertEqual(MathLib.Divide(2/3,-1/3),-2)
		self.assertEqual(MathLib.Divide(-2/3,-1/3),2)
	
	def testPositiveNums(self):
		self.assertEqual(MathLib.Divide(0,1),0)
		self.assertEqual(MathLib.Divide(1,1),1)
		self.assertEqual(MathLib.Divide(100,50),2)
		self.assertEqual(MathLib.Divide(999,1),999)
		self.assertEqual(MathLib.Divide(1,999),1/999)

	def testNegativeNums(self):
		self.assertEqual(MathLib.Divide(0,-1),0)
		self.assertEqual(MathLib.Divide(-10,-90),1/9)
		self.assertEqual(MathLib.Divide(-90,-10),9)
		self.assertEqual(MathLib.Divide(-999,-1),999)
		self.assertEqual(MathLib.Divide(-1,-999),1/999)

	def testPositiveNegativeNums(self):
		self.assertEqual(MathLib.Divide(-1,1),-1)
		self.assertEqual(MathLib.Divide(1,-1),-1)
		self.assertEqual(MathLib.Divide(-90,100),-9/10)
		self.assertEqual(MathLib.Divide(90,-100),-9/10)
		self.assertEqual(MathLib.Divide(100,-90),-10/9)
		self.assertEqual(MathLib.Divide(-100,90),-10/9)


# Test case to verify the correctness of the factorial
# function: Fac(a)
class testFactorial(unittest.TestCase):
	
	def testZeroDivisionErrors(self):
		with self.assertRaises(ZeroDivisionError):
			MathLib.Fac(1/0,1/0)	
		with self.assertRaises(ZeroDivisionError):
			MathLib.Fac(1/0,0)
		with self.assertRaises(ZeroDivisionError):
			MathLib.Fac(0,1/0)

	def testNonNaturalNumbers(self):
		with self.assertRaises(RecursionError):
			MathLib.Fac(-1)
		with self.assertRaises(RecursionError):
			MathLib.Fac(2/-1)
	
	def testNaturalNumbers(self):
		self.assertEqual(MathLib.Fac(0),1)
		self.assertEqual(MathLib.Fac(1),1)
		self.assertEqual(MathLib.Fac(2),2)
		self.assertEqual(MathLib.Fac(3),6)
		self.assertEqual(MathLib.Fac(4),24)
		self.assertEqual(MathLib.Fac(5),120)

# Test case to verify the correctness of the exponentiation
# function: Power(a,b)
class testExponentiation(unittest.TestCase):

	 
	def testZeroDivisionErrors(self):
		with self.assertRaises(ZeroDivisionError):
			MathLib.Power(1/0,1/0)	
		with self.assertRaises(ZeroDivisionError):
			MathLib.Power(1/0,0)
		with self.assertRaises(ZeroDivisionError):
			MathLib.Power(0,1/0)

	def testPositiveNums(self):
		self.assertEqual(MathLib.Power(0,0),1)
		self.assertEqual(MathLib.Power(0,1),0)
		self.assertEqual(MathLib.Power(1,0),1)
		self.assertEqual(MathLib.Power(2,2),4)
		self.assertEqual(MathLib.Power(2,10),1024)
		self.assertEqual(MathLib.Power(100,3),1000000)

	def testNegativeNums(self):
		self.assertEqual(MathLib.Power(-1,0),1)
		self.assertEqual(MathLib.Power(0,-1),0)
		self.assertEqual(MathLib.Power(-2,-2),0.25)
		self.assertEqual(MathLib.Power(-100,-2),0.0001)
		self.assertEqual(MathLib.Power(-100,-3),-0.000001)

	def testPositiveNegativeNums(self):
		self.assertEqual(MathLib.Power(-1,1),-1)
		self.assertEqual(MathLib.Power(1,-1),1)
		self.assertEqual(MathLib.Power(10,-3),0.001)
		self.assertEqual(MathLib.Power(-10,3),-1000)
		self.assertEqual(MathLib.Power(-100,2),10000)
		self.assertEqual(MathLib.Power(100,-2),0.0001)

# Test case to verify the correctness of the Root
# function: Root(a,b)
class testRoot(unittest.TestCase):

	def testZeroDivisionErrors(self):
		with self.assertRaises(ZeroDivisionError):
			MathLib.Root(1/0,1/0)	
		with self.assertRaises(ZeroDivisionError):
			MathLib.Root(1/0,0)
		with self.assertRaises(ZeroDivisionError):
			MathLib.Root(0,1/0)

	def testNegativeRootBase(self):
		with self.assertRaises(ValueError):
			MathLib.Root(-100,2) 
		with self.assertRaises(ValueError):
			MathLib.Root(-1000,3)
		with self.assertRaises(ValueError):
			MathLib.Root(-1,4)

	def testEvenExponents(self):
		self.assertEqual(MathLib.Root(0,2),0)
		self.assertEqual(MathLib.Root(1,2),1)
		self.assertEqual(MathLib.Root(100,2),10)
		self.assertEqual(MathLib.Root(10000,4),10)
		self.assertEqual(MathLib.Root(100,-2),0.1)
		self.assertEqual(MathLib.Root(10000,-4),0.1)

	def testOddExponents(self):
		self.assertEqual(MathLib.Root(0,1),0)
		self.assertEqual(MathLib.Root(1,3),1)
		self.assertEqual(MathLib.Root(1000,3),10)
		self.assertEqual(MathLib.Root(100000,5),10)
		self.assertEqual(MathLib.Root(1000,-3),0.1)
		self.assertEqual(MathLib.Root(100000,-5),0.1)

	def testFloats(self):
		self.assertEqual(MathLib.Root(2,0.1),1024)
		self.assertEqual(MathLib.Root(2,-0.1),1/1024)
		self.assertEqual(MathLib.Root(0.25,2),0.5)
		self.assertEqual(MathLib.Root(0.25,-2),2)
		self.assertEqual(MathLib.Root(0.1,0.1),0.0000000001)


# Test case to verify the correctness of the Sinus
# function: Sin(a,b)
class testSinus(unittest.TestCase):
 
	def testZeroDivisionErrors(self):
		with self.assertRaises(ZeroDivisionError):
			MathLib.Sin(1/0,1/0)	
		with self.assertRaises(ZeroDivisionError):
			MathLib.Sin(1/0,0)
		with self.assertRaises(ZeroDivisionError):
			MathLib.Sin(0,1/0)

	def testPositiveDegrees(self):
		self.assertEqual(MathLib.Sin(0),0)
		self.assertEqual(MathLib.Sin(30),0.5)
		self.assertEqual(MathLib.Sin(90),1)
		self.assertEqual(MathLib.Sin(180),0)
		self.assertEqual(MathLib.Sin(270),-1)
		self.assertEqual(MathLib.Sin(360),0)


	def testNegativeDegrees(self):
		self.assertEqual(MathLib.Sin(-30),-0.5)
		self.assertEqual(MathLib.Sin(-90),-1)
		self.assertEqual(MathLib.Sin(-180),0)
		self.assertEqual(MathLib.Sin(-270),1)
		self.assertEqual(MathLib.Sin(-360),0)


# Test case to verify the correctness of the Cosinus
# function: Cos(a,b)
class testCosinus(unittest.TestCase):
 
	def testZeroDivisionErrors(self):
		with self.assertRaises(ZeroDivisionError):
			MathLib.Cos(1/0,1/0)	
		with self.assertRaises(ZeroDivisionError):
			MathLib.Cos(1/0,0)
		with self.assertRaises(ZeroDivisionError):
			MathLib.Cos(0,1/0)

	def testPositiveDegrees(self):
		self.assertEqual(MathLib.Cos(0),1)
		self.assertEqual(MathLib.Cos(60),0.5)
		self.assertEqual(MathLib.Cos(90),0)
		self.assertEqual(MathLib.Cos(180),-1)
		self.assertEqual(MathLib.Cos(270),0)
		self.assertEqual(MathLib.Cos(360),1)


	def testNegativeDegrees(self):
		self.assertEqual(MathLib.Cos(-60),0.5)
		self.assertEqual(MathLib.Cos(-90),0)
		self.assertEqual(MathLib.Cos(-180),-1)
		self.assertEqual(MathLib.Cos(-270),0)
		self.assertEqual(MathLib.Cos(-360),1)


# Test case to verify the correctness of the absolute value
# function: Abs(a,b)
class testAbs(unittest.TestCase):
 
	def testZeroDivisionErrors(self):
		with self.assertRaises(ZeroDivisionError):
			MathLib.Abs(1/0,1/0)	
		with self.assertRaises(ZeroDivisionError):
			MathLib.Abs(1/0,0)
		with self.assertRaises(ZeroDivisionError):
			MathLib.Abs(0,1/0)
	
	def testFloats(self):
		self.assertEqual(MathLib.Abs(-0.1),0.1)
		self.assertEqual(MathLib.Abs(0.1),0.1)
		self.assertEqual(MathLib.Abs(-0.01),0.01)
		self.assertEqual(MathLib.Abs(0.01),0.01)

	def testPositiveDegrees(self):
		self.assertEqual(MathLib.Abs(0),0)
		self.assertEqual(MathLib.Abs(10),10)
		self.assertEqual(MathLib.Abs(10/5),2)
		self.assertEqual(MathLib.Abs(100),100)

	def testNegativeDegrees(self):
		self.assertEqual(MathLib.Abs(-10),10)
		self.assertEqual(MathLib.Abs(-10/5),2)
		self.assertEqual(MathLib.Abs(-100),100)
		self.assertEqual(MathLib.Abs(-250),250)


# Test case to verify the correctness of the conversion
# from Horse Power to Kilowatts and vice versa: PowerConvert(a,b)
class testPowerConvert(unittest.TestCase):
 
	def testValueErrors(self):
		with self.assertRaises(ValueError):
			MathLib.PowerConvert(10,"Try")	
		with self.assertRaises(ValueError):
			MathLib.PowerConvert(10,10)
		with self.assertRaises(ValueError):
			MathLib.PowerConvert(10,0.01)
	
	def testFloats(self):
		self.assertEqual(MathLib.PowerConvert(0.5,"HP"),0.3728)
		self.assertEqual(MathLib.PowerConvert(0.3728,"KW"),0.5)
		self.assertEqual(MathLib.PowerConvert(-0.5,"HP"),-0.3728)
		self.assertEqual(MathLib.PowerConvert(-0.3728,"KW"),-0.5)

	def testPositiveValues(self):
		self.assertEqual(MathLib.PowerConvert(10,"HP"),7.4570)
		self.assertEqual(MathLib.PowerConvert(7.4570,"KW"),10)
		self.assertEqual(MathLib.PowerConvert(550,"HP"),410.1349)
		self.assertEqual(MathLib.PowerConvert(410.1349,"KW"),550)

	def testNegativeValues(self):
		self.assertEqual(MathLib.PowerConvert(-10,"HP"),-7.4570)
		self.assertEqual(MathLib.PowerConvert(-7.4570,"KW"),-10)
		self.assertEqual(MathLib.PowerConvert(-550,"HP"),-410.1349)
		self.assertEqual(MathLib.PowerConvert(-410.1349,"KW"),-550)


# Test case to verify the correctness of the conversion
# from Horse Power to Kilowatts and vice versa: TorqueConvert(a,b)
class testTorqueConvert(unittest.TestCase):
 
	def testValueErrors(self):
		with self.assertRaises(ValueError):
			MathLib.TorqueConvert(10,"Try")	
		with self.assertRaises(ValueError):
			MathLib.TorqueConvert(10,10)
		with self.assertRaises(ValueError):
			MathLib.TorqueConvert(10,0.01)
	
	def testFloats(self):
		self.assertEqual(MathLib.TorqueConvert(0.5,"NM"),0.3688)
		self.assertEqual(MathLib.TorqueConvert(0.3688,"lbs-ft"),0.5)
		self.assertEqual(MathLib.TorqueConvert(-0.5,"NM"),-0.3688)
		self.assertEqual(MathLib.TorqueConvert(-0.3688,"lbs-ft"),-0.5)

	def testPositiveValues(self):
		self.assertEqual(MathLib.TorqueConvert(10,"NM"),7.3756)
		self.assertEqual(MathLib.TorqueConvert(7.3756,"lbs-ft"),10)
		self.assertEqual(MathLib.TorqueConvert(550,"NM"),405.6592)
		self.assertEqual(MathLib.TorqueConvert(405.6592,"lbs-ft"),550)

	def testNegativeValues(self):
		self.assertEqual(MathLib.TorqueConvert(-10,"NM"),-7.3756)
		self.assertEqual(MathLib.TorqueConvert(-7.3756,"lbs-ft"),-10)
		self.assertEqual(MathLib.TorqueConvert(-550,"NM"),-405.6592)
		self.assertEqual(MathLib.TorqueConvert(-405.6592,"lbs-ft"),-550)

if __name__ == '__main__':
	unittest.main()
