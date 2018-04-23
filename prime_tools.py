from math import sqrt
import json

def prime_table(n):
	'''
	p(n) ～ n/ln(n) , p(n) == len(prs)
	return the prime number from 1 to n
	'''
	if n < 2:
		return []
	elif n < 3:
		return [ 2, ]
	prs = [2,3]
	step = 2
	guess =	 5

	while guess <= n:			
		for p in prs:			
			# +2 ,beacuse math.sqrt is not always accurate
			# p == prs[-1] is useful at first loop
			if p >  sqrt(guess) +2 or (p == prs[-1]):				
				prs.append(guess)
				break
			if guess%p == 0:
				break
		guess += step
	return prs


def prime_table_generator():
	'''
	a generator for [2,3,5,7,...] 
	'''
	prs = [ 2 ]
	yield prs
	prs.append(3)
	yield prs
	step = 2
	guess =	 5

	while True:			
		for p in prs:			
			if p >  sqrt(guess) +2 or (p == prs[-1]):
				prs.append(guess)				
				yield prs
				break
			if guess%p == 0:
				break
		guess += step


def prime_generator():
	'''
	a generator for 2,3,5,7,... 
	'''
	p = 2
	yield p
	p = 3
	yield p
	prs = [2,3]
	step = 2
	guess =	 5

	while True:			
		for p in prs:			
			if p >  sqrt(guess) +2 or (p == prs[-1]):				
				prs.append(guess)				
				yield guess
				break
			if guess%p == 0:
				break
		guess += step


def prime_dict(n):
	'''
	return a dict,its value is  key-th prime number 
	e.g { 1:2 , 2:3 ,3:5,  4:7, ...}
	'''
	pg = prime_generator()
	cache_dict = {}
	i = 0
	while i < n:
		i +=1
		cache_dict[ i ] = next(pg)
	return cache_dict


def test_prime_dict(n):
	pg = prime_generator()
	for i in range(1,n+1):		
		assert prime_dict(n)[i] == next(pg)


def test_prime_generator(n):
	p1 = prime_table(n)
	p2 = prime_generator()
	for p in p1:
		assert next(p2) ==  p


def test_prime_table_generator(n):
	prs = prime_table(n)
	ptg = prime_table_generator()
	print(prs,)
	for p in prs:
		assert p == next(ptg)[-1]


def test_prime_table(n):
	with open('prime_num_lessthan_1M.json','r') as f:
		big_prs= json.loads (f.read())
		prs = prime_table(n)		
		for p1 ,p2 in zip(prs,big_prs):
			assert p1 == p2,'{} != {} '.format(p1,p2)


if __name__ == '__main__':

	#  no error in test

	# test_prime_table(121127)
	# test_prime_generator(3221)
	# test_prime_table_generator(3121)

	# but take 20+s ,whty
	# test_prime_dict(1111)
	pass