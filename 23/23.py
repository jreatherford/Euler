#it took my PC 11.6 seconds to run this...
#...I am ashamed.  I can do better than this.

size = 28123;
factorSum = [0] * size;
abundantMap = [False] * size;

abundantNums = [];
total = 0;

#find the sum of factors for each number
for x in range(1, size):
    for y in range(x*2, size, x):
        factorSum[y] += x;

#find all the abundant numbers
for n in range (1, size):
	if (factorSum[n] > n):
		abundantNums.append(n);
	
#figure out which numbers are the sum of two adundants
#this is where 99% of my processing is...
#...I really should optimize it because 11.6 is just shamefull
for x in abundantNums:
	for y in abundantNums:
		if ((x+y) >= size):
			break;
		else:
			abundantMap[x+y] = True;	

#pick out the ones to add to the total
for z in range (1, size):
	if (abundantMap[z] == False):
		total += z;

print total;