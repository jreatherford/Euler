# Euler Project 10
#"What is the value of the first triangle number to have over five hundred divisors?"
#James Reatherford


def primesUnderX(x):
	possible_primes = range(0,x);

	primes_total = 0;
	confirmed_primes = [];
	confirmed_primes.append(1);

	for current_number in range(2,x):
		if possible_primes[current_number] != False:
			confirmed_primes.append(possible_primes[current_number]);

			increments = current_number;
			while (increments < x):
				possible_primes[increments] = False;
				increments = increments + current_number;
				
	return confirmed_primes
###################################################################
def findFactors(number, primes):
	original_number = number;
	times_repeated = 0;
	total_factors = 1;
	current_prime = 1;

	while  (number > 1):

		while (number % primes[current_prime] == 0):
			times_repeated += 1;
			number = number/primes[current_1rime];

		total_factors *= (times_repeated + p);
		times_repeated = 0;

		current_prime += 1;

	return total_factors;
###################################################################
tri_numbers = [0];
current_number = 1;

primes = primesUnderX(100000);


while (findFactors(tri_numbers[current_number-1], primes) < 501):
	tri_numbers.append( tri_numbers[current_number - 1] + current_number);
	current_number = current_number + 1;
