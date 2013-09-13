size = 10000;
factorSum = [0] * size;

#find the sum of factors for each number
for x in range(1, size):
    for y in range(x*2, size, x):
        factorSum[y] += x;

total = 0;
for n in range (1,size):
    if ((factorSum[n] < size) and (factorSum[n] > 0)):
        if (n == factorSum[factorSum[n]]) and (n != factorSum[n]):
            total += (n);

print total;