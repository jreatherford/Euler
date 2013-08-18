# Euler Project 10
# Find the sum of all primes under 2,000,000
#James Reatherford

limit = 2000000;
possible_primes = range(0,limit);

primes_total = 0;
confirmed_primes = [];


for current_number in range(2,limit):
	if possible_primes[current_number] != False:
		confirmed_primes.append(possible_primes[current_number]);

		increments = current_number;
		while (increments < limit):
			possible_primes[increments] = False;
			increments = increments + current_number;

for current_prime in confirmed_primes:
	primes_total = primes_total + current_prime; 

print primes_total;