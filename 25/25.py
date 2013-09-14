#there is some pattern here.  the number to the next term always increases by 4 or 5 (after 2 digits)
#I just can't quite see the pattern for if it increases by 4 or 5...I know I am close...just not quite there yet

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