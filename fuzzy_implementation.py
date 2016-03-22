# Leah Robert	1002 3914		1ler1@queensu.ca
# CISC 490: 		Fuzzy Logic Implementation
# Winter		2016

# Libraries/Modules used:
# Sympy library (which needs mpmath library)
from decimal import Decimal
import sympy
import re

a = sympy.symbols('a')
b = sympy.symbols('b')
c = sympy.symbols('c')
d = sympy.symbols('d')		# variable x
e = sympy.symbols('e')
f = sympy.symbols('f')
g = sympy.symbols('g')
h = sympy.symbols('h')
x = sympy.symbols('x')		# variable y
p = sympy.symbols('p')		# denotes alpha

binary_list = ['add', 'subtract', 'multiply', 'divide']
mem_list = {}
bin_list = {}

def getMembership(mf, x):
	left = mf[0]
	right = mf[1]
	if x < left[0]:
		return 0

# Fill x into the given membership function	
def fillInX(mf, x):
	left= mf[0]
	right = mf[1]
	left = left.replace('x', x)
	right = right.replace('x', x)
	return [left, right]

# Fill in the values for each variable
def fillInValues(memName, values):	
	mf = mem_list[memName]
	left = mf[0]
	right = mf[1]
	varList = ['a','b','c','d','e','f','g','h']
	for i in range(8):
		left = left.replace(varList[i], values[i])
		right = right.replace(varList[i], values[i])
	result = [left, right]
	print(result)
	return result

# Determine the membership of a value x in a given saved membership function
def determineMembership():
	mf = input('Which saved membership function would you like to access? ')
	if mf not in mem_list:
		error('Invalid membership function name. ')
		return
	if mf in bin_list:
		xValues = input('Please input your fuzzy values for X: (e.g.) a b c d \n')
		yValues = input('Please input your fuzzy values for Y: (e.g.) e f g h \n')
		x = input('Please input your value for x: ')
		values =  xValues.split() + yValues.split()
		result = fillInValues(mf, values)
		result = fillInX(result, x)
		final = getMembership(result, x)
		print(eval(result[0]))
		print(eval(result[1]))
		
	else:
		pass
	
	

# Take the inverse of a fuzzy number and determine the resulting membership function
def inverse(xL, xR):
	left = '1 /' + xL
	right = '1 /' + xR
	left = sympy.sympify(left)
	right = sympy.sympify(right)
	left = rearrangeExp(x, left, p)
	right = rearrangeExp(x, right, p)
	print(left)
	print(right)
	inp = save()
	if inp != 'no':
		mem_list[inp] = [left, right]

def squareRoot(xL, xR):
	left = 'sqrt(' + xL + ')'
	right = 'sqrt(' + xR + ')'
	left = sympy.sympify(left)
	right = sympy.sympify(right)
	left = rearrangeExp(x, left, p)
	right = rearrangeExp(x, right, p)
	print(left)
	print(right)
	inp = save()
	if inp != 'no':
		mem_list[inp] = [left, right]

# Use interval arithmetic and divide the two fuzzy numbers to determine the membership function
def divide(xL, xR, yL, yR):
	left = xL + '/' + yR
	right = yL + '/' + xR
	left = sympy.sympify(left)
	right = sympy.sympify(right)
	left = rearrangeExp(x, left, p)
	right = rearrangeExp(x, right, p)
	print(left)
	print(right)
	inp = save()
	if inp != 'no':
		mem_list[inp] = [left, right]
		bin_list[inp] = [left, right]

# Use interval arithmetic and multiply the two fuzzy numbers to determine the membership function
def multiply(xL, xR, yL, yR):
	left = xL + '*' + yR
	right = yL + '*' + xR
	left = sympy.sympify(left)
	right = sympy.sympify(right)
	left = rearrangeExp(x, left, p)
	right = rearrangeExp(x, right, p)
	print(left)
	print(right)
	inp = save()
	if inp != 'no':
		mem_list[inp] = [left, right]
		bin_list[inp] = [left, right]

# Use interval arithmetic and subtract the two fuzzy numbers to determine the membership function
def subtract(xL, xR, yL, yR):
	left = xL + '-' + yR
	right = yL + '-' + xR
	left = sympy.sympify(left)
	right = sympy.sympify(right)
	left = rearrangeExp(x, left, p)
	right = rearrangeExp(x, right, p)
	print(left)
	print(right)
	inp = save()
	if inp != 'no':
		mem_list[inp] = [left, right]
		bin_list[inp] = [left, right]

# Use interval arithmetic and add the two fuzzy numbers to determine the membership function
def add(xL, xR, yL, yR):
	left = xL + '+' + yL
	right = xR + '+' + yR
	left = sympy.sympify(left)
	right = sympy.sympify(right)
	left = rearrangeExp(x, left, p)
	right = rearrangeExp(x, right, p)
	print(left)
	print(right)
	inp = save()
	if inp != 'no':
		mem_list[inp] = [left, right]
		bin_list[inp] = [left, right]

# Main program that takes in an operator and does the calculation
def start(xL, xR):
	count = 0
	op = ''
	while(op != 'exit'):
		op = input('What operator would you like to use? ')
		if op in binary_list and count == 0:
			yL = getLeftMembershipFunction('(x-e)/(f-e)')
			yR = getRightMembershipFunction('(h-x)/(h-g)')
			mem_list['Y'] = [yL, yR]
			print('Refer to this fuzzy number as \'Y\'')
			count = count + 1
		
		if op == 'add':
			add(xL, xR, yL, yR)
		elif op == 'subtract':
			subtract(xL, xR, yL, yR)
		elif op == 'multiply':
			multiply(xL, xR, yL, yR)
		elif op == 'divide':
			divide(xL, xR, yL, yR)
		elif op == 'square root':
			squareRoot(xL, xR)
		elif op == 'inverse':
			inverse(xL, xR)
		elif op == 'exponent':
			pass
		elif op == 'logarithm':
			pass
		elif op == 'membership':
			determineMembership()
		elif op == 'exit':
			pass
		else:
			error('Invalid operator ')

def save():
	print('Shall we save this membership function to be used again?')
	inp = input('If yes, please give it a name. If no, type \'no\' ')
	return inp

def fixExp(exp):
	exp = str(exp)
	exp = exp.replace('[', '(')
	exp = exp.replace(']', ')')
	return exp

# Rearranges the equation to be in terms of var
def rearrangeExp(left, right, var):
	L = left
	result = sympy.solve(L-right, var)
	L = var
	result = fixExp(result)
	return result

# This puts the inputted string in an expression form, rearranged for x
def fixInput(str):
	sympified = sympy.sympify(str)
	rearranged = rearrangeExp(p, sympified, x)
	return rearranged

def getLeftMembershipFunction(str):
	#inp = input('What is your membership function for the a <= x <= b portion?')
	# TODO - fix so it accepts a function
	inp = '(x-a)/(b-a)'
	xL = fixInput(str)
	return xL
	
def getRightMembershipFunction(str):
	#inp = input('What is your membership function for the c <= x <= d portion?')
	# TODO - fix so it accepts a function
	inp = '(c-x)/(c-b)'
	xR = fixInput(str)
	return xR

def error(msg):
	print('Error: ' + msg)

def main():
	#printExample()
	xL = getLeftMembershipFunction('(x-a)/(b-a)')
	xR = getRightMembershipFunction('(d-x)/(d-c)')
	mem_list['X'] = [xL, xR]
	print('Refer to this fuzzy number as \'X\'')
	start(xL, xR)

main()







# Add two fuzzy numbers together
#def add(listX, listY):
#	lenX = len(listX)
#	print(lenX)
#	lenY = len(listY)
#	listZ = [0,0,0]
#	for i in range(3):
#		listZ[i] = listX[i] + listY[i]
#	if (lenX == 3 and lenY == 3):
#		return listZ
#	elif (lenX == 4 and lenY == 4):
#		pass

# Determine the membership of value x in a given fuzzy number
def membership(x, lowerbound, middle, upperbound):
	if (x >= lowerbound and x <= middle):
		y = (x - lowerbound) / (middle - lowerbound)
	elif (x >= middle and x <= upperbound):
		y = (upperbound - x) / (upperbound - middle)
	else:
		y = 0
	y = round(y, 2)
	return y

# Print an example fuzzy number in both triangle and trapezoidal form
def printExample():
	print('This program can take in a triangular or trapezoidal fuzzy number of the form:')
	print('Triangular fuzzy number, where b = c: ')
	print('          b,c          ')
	print('         /   \         ')
	print('        /     \        ')
	print('       /       \       ')
	print('      /         \      ')
	print('     a           d     ')
	print('')
	print('Trapezoidal fuzzy number: ')
	print('          b ------- c             ')
	print('         /              \         ')
	print('        /                \        ')
	print('       /                  \       ')
	print('      /                    \      ')
	print('     a                      d     ')