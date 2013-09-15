#taking a new approach...

# I am 98% sure this code would find it... 
#...but I keep getting an overflow error because apparently, python can't handle thousand digit numbers

import math;
for n in range (4000,5000):
	if (((pow((1 + math.sqrt(5)),n) - pow((1 - math.sqrt(5)),n))/(pow(2,n)*math.sqrt(5))) >= 1e999):
		print n;
		break;

print "done";

#I bascially took this formula and threw it into wolfwarm alpha, changing n by basically doing binary search 
# and now I know the answer is 4782...but I wanna be able to compute it on my own before I throw it into
# project euler 