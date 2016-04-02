# Leah Robert	1002 3914		1ler1@queensu.ca
# CISC 490: 		Fuzzy Logic Implementation
# Winter		2016

# Libraries/Modules used:
# Sympy library (which needs mpmath library)
from decimal import Decimal
import sympy
import re

DEFAULT_X = '(x-a)/(b-a)'
DEFAULT_Y = '(c-x)/(c-b)'

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

# Determine the membership of x in the membership function
def getMembership(mf, x, values):
	left = mf[0]
	right = mf[1]
	if eval(left) <= 1 and eval(left) >= -1:
		return round(eval(left), 2)
	elif eval(right) <= 1 and eval(right) >= -1: 
		return round(eval(right), 2)
	else:
		return 0

# Fill x into the given membership function	
def fillInX(mf, x):
	left= mf[0]
	right = mf[1]
	left = left.replace('x', x)				# replace all instances of x in the formula with the value of x
	right = right.replace('x', x)
	return [left, right]

# Fill in the values for each variable
def fillInValues(memName, values):	
	mf = mem_list[memName]
	left = mf[0]
	right = mf[1]
	varList = ['a','b','c','d','e','f','g','h']
	for i in range(len(values)):
		left = left.replace(varList[i], values[i])
		right = right.replace(varList[i], values[i])
	left = str(sympy.simplify(left))
	right = str(sympy.simplify(right))
	return [left, right]

# Determine the membership of a value x in a given saved membership function
def determineMembership():
	print('These are the current membership functions you have saved: ')
	for item in mem_list:
		if (item != 'Y' and item != 'X'):
			print(item)								# currently saved membership names
	mf = input('Which saved membership function would you like to access? ')
	if mf not in mem_list:
		error('Invalid membership function name. ')			# not a currently saved membership name
		return
	if mf in bin_list:
		xValues = input('Please input your fuzzy values for X: (e.g.) a b c d \n')
		yValues = input('Please input your fuzzy values for Y: (e.g.) e f g h \n')
		x = input('Please input your value for x: ')
		values =  xValues.split() + yValues.split()
		#printNumber(values[0], values[1], values[2], values[3])
		result = fillInValues(mf, values)						# values to fill in for a, b, c, d for both the X and Y membership functions
		result = fillInX(result, x)							# fill X into the membership function
		final = getMembership(result, x, values)
	else:
		xValues = input('Please input your fuzzy values for X: (e.g.) a b c d \n')
		x = input('Please input your value for x: ')
		values =  xValues.split()
		result = fillInValues(mf, values)
		result = fillInX(result, x)
		final = getMembership(result, x, values)
	print('The membership of x is: ' + str(abs(final)))

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

# Take the square root of a fuzzy number and determine the resulting membership function
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
	left = '-(' + xL + '/' + yR + ')'
	right = '-(' + yL + '/' + xR + ')'
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
	left = '-(' + xL + '-' + yR + ')'
	right = '-(' + yL + '-' + xR + ')'
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

# Main program that takes in an operator and does some calculation
def start(xL, xR):
	count = 0
	op = ''
	while(op != 'exit'):
		print('=========================================================')
		print('These are the possible operators: ')
		print('add subtract multiply divide sqrt inverse mbrshp exit')
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
		elif op == 'sqrt':
			squareRoot(xL, xR)
		elif op == 'inverse':
			inverse(xL, xR)
		elif op == 'exponent':
			pass
		elif op == 'logarithm':
			pass
		elif op == 'mbrshp':
			determineMembership()
		elif op == 'exit':
			pass
		else:
			error('Invalid operator ')


# Asks if the user wants to 'save' their membership function to use later
def save():
	print('Shall we save this membership function to be used again?')
	inp = input('If yes, please give it a name. If no, type \'no\' ')
	return inp

# Change all square brackets to be the corresponding round brackets
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

# Get the left membership function for a fuzzy number (parameter is default)
def getLeftMembershipFunction(str):
	inp = input('What is your membership function for the a <= x <= b portion? (\'def\' for default) ')
	if inp == 'def':
		inp = str
	xL = fixInput(inp)
	return xL

# Get the right membership function for a fuzzy number (parameter is default)
def getRightMembershipFunction(str):
	inp = input('What is your membership function for the c <= x <= d portion? (\'def\' for default)')
	if inp == 'def':
		inp = str
	xR = fixInput(inp)
	return xR

# Prints an error message
def error(msg):
	print('Error: ' + msg)

def printNumber(a, b, c, d):
	if b == c:
		print('          ' + b + '           ')
		print('         /   \         ')
		print('        /     \        ')
		print('       /       \       ')
		print('      /         \      ')
		print('     ' + a + '           ' + d + '     ')
		print('')
	else: 
		print('          ' + b + ' ------- ' + c + '             ')
		print('         /              \         ')
		print('        /                \        ')
		print('       /                  \       ')
		print('      /                    \      ')
		print('     ' + a + '                      '+ d + '     ')

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