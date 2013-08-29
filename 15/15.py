import math;

square_size = 20;

k_factorial = 1;
n_factorial = 1;

for i in range (1, ((square_size*2)+1)):
	n_factorial *= i;
	if (i == square_size):
		k_facotrial = n_factorial;

paths = n_factorial/math.pow(k_facotrial,2);

print long(paths);