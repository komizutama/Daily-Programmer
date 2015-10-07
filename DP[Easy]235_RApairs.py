#solves https://redd.it/3nkanm

def Factor_Num(n):
	#Factors a number.
	facList = []
	for i in range(1,n):
		if n % i == 0:
			facList.append(i)
	return facList

def is_Prime(l):
	#Checks whether a nuumber is prime.
	if l in (1,2):
		return True
	for a in range(2,l):
		if l % a == 0:
			return False
	return True

def priFacs(n):
	#Calculates the prime factors of a number.
	pFacs = []
	for i in Factor_Num(n):
		if is_Prime(i):
			pFacs.append(i)
	return pFacs


def RAComp(x,y):
	#Checks whether an input pair of numbers is a Ruth-Aaron pair
	xRA=sum(priFacs(x))
	yRA=sum(priFacs(y))
	print xRA
	print yRA

	if xRA == yRA:
		return "("+ str(x)+ "," +str(y)+ ") "+ "VALID"
	else:
		return "("+str(x)+","+str(y) + ") "+ "NOT VALID"

print RAComp(714,715)
print RAComp(77,78)
print RAComp(20,21)




