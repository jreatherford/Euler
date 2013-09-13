#trimmed down from 11.6s to 8.3

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
	
#find all the sum of abundant numbers:
#   this is where 98% of the processing goes
#   I modified the loop enough to trim it down to 8.3s
stop_point = len(abundantNums);
for x in range(0, len(abundantNums)):
	for y in range(x, stop_point):
		sum = abundantNums[x]+abundantNums[y];
		if (sum >= size):
			stop_point = y;
			break;
		else:
			abundantMap[sum] = True;	

#pick out the ones to add to the total
for z in range (1, size):
	if (abundantMap[z] == False):
		total += z;

print total;