import random

length = 3

sides = 5

numbers = [1,2,3,4,5,6,7,8,9,10]

largestGon ='0'

def recursion():
	global largestGon
	counter = 0
	gon = list(numbers)
	possibleNumbers = list(numbers)
	random.shuffle(gon)
	#print gon
	while counter < 10:
		random.shuffle(gon)
		while not checkSums(gon):
			random.shuffle(gon)
		while 10 not in gon[0:5]:
			random.shuffle(gon)
		counter += 1	
		thisGon = getConcatNum(gon)	
		if int(largestGon) < int(thisGon):
			largestGon = thisGon
#	print gon
#	print getConcatNum(gon)
#	print sumLength(gon,0)
	print largestGon
		
		

def checkSums(gon):
	sum = sumLength(gon, 0)
	#print sum
	for i in range(sides):
		if sumLength(gon, i) != sum:
#			print sumLength(gon, i)
			return False
	return True 

def sumLength(gon, index):
	return gon[index] + gon[index + sides] + gon[sides + (index+sides+1) % sides]

def stringSum(gon, index):
	#print 'index: ' + str(index)
	return str(gon[index]) + str(gon[index+sides]) + str(gon[sides + (index+sides+1)% sides])

def getConcatNum(gon):
	resultNum = ""
	startIndex = 0
	for i in range(sides):
		if gon[i] < gon[startIndex]:
			startIndex = i
	for i in range(sides):
		resultNum += stringSum(gon,startIndex)
		startIndex = (startIndex + 1) % sides
	return resultNum

def getOrderedGon(gon):
	newGon=[0,0,0,0,0,0]
	startIndex = 0
	for i in range(sides):
		if gon[i] < startIndex:
			startIndex = i



#checkSums(ngon)
recursion()
