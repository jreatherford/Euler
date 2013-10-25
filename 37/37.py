def findPrimes(size, prime_table):
    primes = []
    for i in range (2, size + 1):
        if prime_table[i] == True:
            primes.append(i)
            for j in range (2*i, size + 1, i):
                prime_table [j] = False
    return primes
    
def isTruncatable (num, prime_table):
    if prime_table[num] == False:
        return False
    if num < 10:
        return False    
    L = num
    R = num
    while (L >= 10):
        L = L/10
        R = int((str(R)[1:]))

        if prime_table[L] == False:
            return False
        if prime_table[R] == False:
            return False
    return True
    
size = 1000000
prime_table = [True] * (size + 1)
prime_table[1] = False
primes = findPrimes(size, prime_table)
total = 0

for i in primes:
    if isTruncatable(i,prime_table) == True:
        total += i
print total
