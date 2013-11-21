fracts = [1] * 101
val = 1
for i in range (1,101):
    val *= i
    fracts[i] = val
    
total = 0

for n in range(2,101):
    for r in range (1,n+1):
        c = fracts[n]/(fracts[r]*fracts[(n-r)])
        if (n == 23 and r == 10):
            print c
        if (c > 1000000):
            total += 1

print total


