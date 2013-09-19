def findCycle(denom):
    divisors = [];
    num = 10;

    while (num%denom != 0):
        divisors.append(num);
        num = (num%denom)*10;
        for currDiv in range(0, len(divisors)):
           if (divisors[currDiv] == num):
               return (len(divisors) - currDiv);
    return 0;

bigN = 0;
bigCycle = 0;

for n in range (1001, 1, -1):
    cycle = findCycle(n);
    if (cycle > bigCycle):
        bigCycle = cycle;
        bigN = n;

print bigN;
