input_file = open("input.txt");

numbers = input_file.readlines();

sum = 0;

for line in numbers:
	sum = (sum + int(line));

print sum;
