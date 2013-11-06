import sys

def genCoprimePairs (max):
    pairs = coprimeHelp (2,1, max)
    return sorted(pairs)
    
def coprimeHelp (m, n, max):
    pairs = [(m,n)]
    
    if (m <= max): 
        pairs.extend(coprimeHelp ((2*m - n), m, max))
        pairs.extend(coprimeHelp ((2*m + n), m, max))
        pairs.extend(coprimeHelp ((m + 2*n), n, max))
    
    return pairs


size = pow(10,4)
coprimes = genCoprimePairs(size)
print len(coprimes)
print "done"
#R_set = {}

#for pair in coprimes:
#    R_set[pair[0]] = 1.0/(pair[0]*pair[1])
    
#print R_set
    



