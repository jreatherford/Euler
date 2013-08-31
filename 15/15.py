import math;

#Bascially, I am using the function for "n choose k" which is n!/k!(n-k)! However, since it is a square and n = 2k,
#it can be simplified as n!/(k!)^2.  For more info on this formula, see the following http://en.wikipedia.org/wiki/Combination

square_size = 20;

k_factorial = 1;
n_factorial = 1;

for i in range (1, ((square_size*2)+1)):
	n_factorial *= i;
	if (i == square_size):
		k_facotrial = n_factorial;

paths = n_factorial/math.pow(k_facotrial,2);

print long(paths);