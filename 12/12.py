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
	total_factors = 1;
	current_prime = 1;
	while ((number > 1) and (current_prime < len(primes))):
		if (number%primes[current_prime] == 0):
			number = number/primes[current_prime]
			total_factors = total_factors + 1;
		else:
			current_prime = current_prime + 1;
	return total_factors;


###################################################################
tri_numbers = [0];
current_number = 1;

print "start-";

while (findFactors(tri_numbers[current_number-1], primes) < 499):
	tri_numbers.append( tri_numbers[current_number - 1] + current_number);
	current_number = current_number + 1;

print tri_numbers[current_number-1];

print "done";