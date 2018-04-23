from prime_tools import prime_table


def isCalcByFunction(n):	
	checklist = [x for x in prime_table(n) if x not in (2,3,5)]
	for p in checklist:
		if n%p == 0:
			return False
	return True


def test(k):
	i = 0
	value = 0
	values =[]
	while i <k:
		value +=1
		if isCalcByFunction(value):
			i+=1			
			values.append(value)
	return values


def main(k):
	i = 0
	num = 0
	while i <k:
		num +=1
		if isCalcByFunction(num):
			i+=1			
	return num	

# Calculating main(112) takes 3.7s with py3 on my PC
# print(main(112))
