

def findFactors (number, factor_table, primes):

	original_number = number;
	times_repeated = 0;
	total_factors = 1;
	current_prime = 1;

	while  (number > 1):

		while (number % primes[current_prime] == 0):
			times_repeated += 1;
			number = number/primes[current_prime];

		total_factors *= (times_repeated + 1);
		times_repeated = 0;

		current_prime += 1;

	return total_factors;

number = 15;
factor_table = [0] * number;
primes = [1,2,3,5,7,11,13];

print findFactors (2, factor_table, primes);
print findFactors (4, factor_table, primes);
print findFactors (6, factor_table, primes);
print findFactors (12, factor_table, primes);

print factor_table;

			#ignore for now
			#divisor = number/primes[current_prime]
			#if (divisor == 1):
			#	number = 1;
			#	total_factors += 1;
			#elif (factor_table[divisor] != 0):
			#	total_factors += (factor_table[divisor]);
			#	number = number/divisor;
			#else:
				#number = number/primes[current_prime];