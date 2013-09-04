
def count_number(number):
	digits = [0,3,3,5,4,4,3,5,5,4,3,6,6,8,8,7,7,9,8,8]; #digits under 20
	tens = [0,0,6,6,5,5,5,7,6,6]; #twenty, thrirty, etc.,

	total = 0;

	if (number > 1000):
		return -1;
	if (number == 1000):
		return 11;

	if (number >= 100):
		total += digits[number/100];
		total += 7; #"hundred"
		number = number%100;
		if (number != 0):
			total += 3; #and


	if (number >= 20):
		total += tens[number/10];
		total += digits[number%10];
	else:
		total += digits[number];

	return total;

grand_total = 0;

for i in range (1,1001):
	grand_total += count_number(i);

print grand_total;

print count_number(115);
		


		


