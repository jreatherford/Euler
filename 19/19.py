day = 1; #0 is sunday, 1 is monday... 
total_sundays = 0;

for year in range(1900, 2001):
	for month in range(1, 13):

		if (day == 0) and (year > 1900):
			total_sundays += 1;

		if (month == 2):
			if ((year%4 == 0) and (year%100 != 0)) or ((year%4 == 0) and (year%400 == 0)):
				day = (day + 29)%7
			else:
				day = (day + 28)%7
		elif (month == 4) or (month == 6) or (month == 9) or (month == 11):
			day = (day + 30)%7
		else:
			day = (day + 31)%7;
			
print total_sundays;