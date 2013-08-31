import math;

power = int(math.pow(2,1000));

place = 1;
total = 0;

while (power/place > 0):
	place *= 10;
	total += (power%place)*10/(place);

print total;