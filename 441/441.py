def genCoprimePairs (max):
    coPrimes = [(2,1)]
    i = 0
    while i < len(coPrimes):
	    m = coPrimes[i][0]
	    n = coPrimes[i][1]

	    if ((2*m - n) <= max): 
	    	coPrimes.append(((2*m - n), m))
	    if ((2*m + n) <= max): 
	    	coPrimes.append(((2*m + n), m))
	    if ((m + 2*n) <= max): 
	    	coPrimes.append(((m + 2*n), n))
	    i += 1   
    return coPrimes

size = pow(10,3)
coPrimes = genCoprimePairs(size)


print "done"
    



