from math import sqrt
from prime_tools import prime_table,prime_table_generator


def natural_num_generator( first_num=0 ):
	while True:
		yield first_num
		first_num +=1


def prime_filter_generator01( ):
	# 321st value is 112500, it takes 13.8s in my PC
	# 221st value is 24000, 1.1s in my PC
	ptg = prime_table_generator( )
	next(ptg)
	next(ptg)
	next(ptg)
	#  remain  2,3,5 
	prime_list = next(ptg)[3:]

	# prime_list = prime_table(20000)[3:]

	num = 1
	while True:		
		flag = True
		for prime in prime_list:
			if num < prime:
				break			
			if num % prime == 0 :
				flag = False
				break
		# if no break				
		if flag:
			yield num
		num += 1
		if prime_list[-1] < num:				
			prime_list = next(ptg)[3:]


def prime_filter_generator02( n ):
	nng = natural_num_generator(1)	
	prime_list = prime_table( n )[3:]

	for num in nng:
		flag = True		
		for prime in prime_list:
			if num  < prime:
				break
			if num % prime == 0 :
				flag = False
				break
		if flag:
			yield num
		if n < num: 
			break


def test_generator(upperLimit,*generators):
	i = 0
	g1 = prime_filter_generator01()
	g2 = prime_filter_generator02(50000)
	while i< upperLimit:
		assert next(g1) == next(g2)
		i+=1


def main(k,a_generator= prime_filter_generator01,*args,**kwargs):
	# k = 121331 ,it will take 6.5s in my pc 
	pfg = a_generator( *args,**kwargs )
	for i in range( k-1 ):
		print(next( pfg ))
	r = (next( pfg ))
	print(r)
	return r


if __name__ == '__main__':
	# comparing  
	# main(221,prime_filter_generator01)
	# main(221,prime_filter_generator02,2211)
	
	#  1.7s
	# main( 571,prime_filter_generator02, 32256 )
		
	# no error in test
	# test_generator(200)

	pass










# def prime_filter_generator_old( remain=( 2,3,5 ) ):
# 	#  yield
# 	nng = natural_num_generator(1)
# 	ptg = prime_table_generator()
# 	for n in remain:
# 		next(ptg)
# 	prime_list = next(ptg)[3:]
# 	for num in nng:
# 		while  prime_list[-1] < num:
# 			prime_list = next(ptg)[3:]
# 		for prime in prime_list:
# 			if num % prime == 0:
# 				break
# 		else:
# 			yield num	


# def filter_generator( k,remain=( 2,3,5 ) ):
# 	nng = natural_num_generator(1)
# 	ptg = prime_table_generator()
# 	prime_list = next(ptg)
# 	while prime_list[-1] < k:
# 		next(ptg)
# 	prime_list = next(ptg)[ 3: ]	

# 	for num in nng:		
# 		for prime in prime_list[:int(sqrt(num)+2)]:
# 			if num % prime == 0 :
# 				break
# 		else:
# 			yield num