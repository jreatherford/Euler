limit = 1000000
total = 0

prime_seive = [True]*limit
confirmed_primes = []
for i in range (2, limit):
	if (prime_seive[i] == True):
		confirmed_primes.append(i);
		for j in range (i*2,limit,i):
			prime_seive[j] = False;

for current_prime in confirmed_primes:
	isCircle = True
	power = len(str(current_prime))

	if (power==1):
		total += 1
	else:
		for i in range (0, power-1):
			if ((current_prime/10) % 10 == 0):
				isCircle = False
				break

			tmp = current_prime%10
			current_prime = (current_prime/10) + (tmp * pow(10,power-1))

			if (prime_seive[current_prime] == False):
				isCircle = False

		if (isCircle == True):
			total += 1

print total;