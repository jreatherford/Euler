#there is some pattern here.  the number to the next term always increases by 4 or 5 (after 2 digits)
#I just can't quite see the pattern for if it increases by 4 or 5...I know I am close...just not quite there yet

fours = 0;
fives = 0;
sample = 309;
digits = 1e1;
prev_count =0;
for bits in range(1,sample):

	fib_gen = [1,1,2];
	cursor = 0;
	term = 3;
	count = 0;
	digits = pow(10, bits);

	while (fib_gen[(cursor-1)%3] < digits):

		if (fib_gen[cursor] > 1e100):
			fib_gen[0] /= 1e80;
			fib_gen[1] /= 1e80;
			fib_gen[2] /= 1e80;
			digits /= 1e80;

		fib_gen[cursor] = fib_gen[(cursor + 1)%3] + fib_gen[(cursor + 2)%3];
		term += 1;
		cursor = (cursor + 1)%3;
		count += 1;

	#print fib_gen;
	if ((count-prev_count) == 4):
		fours += 1;
	else:
		fives += 1;
		#print term, "(", (count-prev_count),")";
	prev_count = count;

	#print term;
	#print "fours", fours, " fives:", fives;
	print float((fours * 4) + (fives * 5))/float(sample);
	#print "-------------------------------------------------"

current_term = 7
total_fives = 2;
current_five = 1;
digits = 2;

while (digits < 1000):
	if current_five > total_fives:
		current_term += 4;
		if (total_fives < 4):
			total_fives += 1;
		else:
			total_fives = 3;
		current_five = 1;
	else:
		current_term += 5;
		current_five += 1;
	digits += 1;

print current_term;