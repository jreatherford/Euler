def findPrimes(size, prime_table):
    primes = []
    for i in range (2, size + 1):
        if prime_table[i] == True:
            j = 2 * i
            while (j < size):
                prime_table [j] = False
                j += i

size = 100000000
prime_table = [True] * (size + 1)
prime_table[1] = False
findPrimes(size, prime_table)

prime_diags = 0
total_diags = 1

len = 2
cursor = 1

ratio = 1.0

while (ratio > .1):
    for j in range (0,4):
        cursor += len
        
        if prime_table[cursor]:
            prime_diags += 1
            
        total_diags += 1    
    ratio = float(prime_diags)/float(total_diags)
    len += 2
    
print len - 1
print ratio