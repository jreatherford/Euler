#I tried to be fancy and do it without brute forcing...
#eventually gave up and decided to try brute force (in the other file)
#turns out, it ran pretty damn fast.  I feel stupid for wasting all day on this
#on the bright side, I learned about sets in python today! :D

total = 0
max = 100
min = 2

primeTable = [True] * (max + 1)
primes = []

for i in range (2,(max + 1)):
    if (primeTable[i] == True):
        primes.append(i);
        for j in range (i*2, max+1, i):
            primeTable[j] = False;

for a in range (min,max+1):
    c = a
    for b in range (min,max+1):
        c *= a
        if (c <= max):
            if (primeTable[b] == True):
                for i in range(b*2,(max+1),b):
                    total += 1


result = (((max+1)-min)**2)-total;

print total;
print result
