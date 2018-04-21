from math import log


countOneFactor = lambda n, base: int( log( n, base ) )


def countFactors(n,*factors):
    if len(factors) ==1:
        return countOneFactor(factors)

    theSum=0
    remainFactors = factors

    maxFactor = max( factors )
    remainFactors.remove(maxFactor)
    minExp = countOneFactor( maxFactor )
    for i in range(1,minExp):
        n = n/maxFactor
        theSum += countFactors(n,*remainFactors )
    return theSum


def count__(n):
    return sum(
        countOneFactor( n,2 ),
        countOneFactor( n,3 ),
        countOneFactor( n,5 ),

        countFactors ( n,2,3),
        countFactors ( n,3,5),
        countFactors ( n,2,5),

        countFactors ( n,2,3,5),
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
