from countFactors import count__


def mnl_upper( k ):
	cubic_root = int(pow(k,1/3)) + 1
	nml = ( 
		cubic_root -1,
		cubic_root -1,
		cubic_root -1,
	 )
	return nml


def new_count(n):
	if n == 1:
		return 1
	a,b = count__(n),count__(n-1)
	if a == b+1:
		return count__(n)
	else:
		return count__(n) + 0.1


calcFunction = lambda n,m,l: (2**n)*(3**m)*(5**l)


def main( k ):
	# binary search
	guess=mnl_upper 
	high = calcFunction( *guess(k) )
	low  = k
	while True:
		value = ( high + low ) // 2
		# print('high,value,low',high,value,low)
		guess_k = new_count( value )
		if guess_k > k:
			high = value
		elif guess_k < k:
			low = value
		else:
			return value

print(main(1000))			
# it takes 21.1s ,the answer is 110536959860366672658432
# print(main(22321))

# it takes 133.8s on my pc py3, 
#the answer: 290142196707510978317649825651773931520
# print(main(100000))