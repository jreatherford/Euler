factorial = 1;
for n in range (1, 101):
	factorial *= n;

total = 0;
string_factorial = str(factorial);

for n in range(0,len(string_factorial)):
	total+= int(string_factorial[n]);

print total;