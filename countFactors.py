def countOneFactor(n,base):
	'''math.log may not be accurate'''
	i = 0
	while base <=n:
		n /= base
		i += 1
	return i


def countFactors(n,*factors):
    if len(factors) ==1:
        return countOneFactor(n,*factors)

    theSum = 0
    remainFactors = list(factors)

    maxFactor = max( factors )
    remainFactors.remove(maxFactor)
    minExp = countOneFactor( n,maxFactor )
    while ( min(remainFactors ) <= (n/maxFactor)):
    # 	pass
    # for i in range(minExp):
        n = n/maxFactor
        theSum += countFactors(n,*remainFactors )
    return theSum


def count__(n):
    return 1+sum( 
    	[
        countOneFactor( n,2 ),
        countOneFactor( n,3 ),
        countOneFactor( n,5 ),

        countFactors ( n,2,3),
        countFactors ( n,3,5),
        countFactors ( n,2,5),

        countFactors ( n,2,3,5),
        		]
    )


def main(k):
    # binary search
    high = 2 ** k
    low =  k
    middle = int((high + low)/2)

    while high > low:
        guess = count__(  middle )
        if guess > k:
            high = middle
        elif guess <k:
            low = middle
        else:
            return middle

# log(N), only 1.0s for this 106 digits num
print(count__( 5464487848945489156189461516554675548454545545564645645644564564564564654564564564564564564897843131547846 ) )
# print( count__(17725876239305002191858) )