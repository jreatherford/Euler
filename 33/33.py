num_product = 1;
denom_product = 1;

for denom in range (11,100):
    for num in range (1,denom):
        num2 = 1
    	denom2 = 1
    	if (num%10 == denom%10) and (denom%10 != 0):
        	num2 = num/10
        	denom2 = denom/10
    	elif (num/10 == denom/10)and (denom%10 != 0):
        	num2 = num%10
        	denom2 = denom%10
    	elif (num%10 == denom/10)and (denom%10 != 0):
        	num2 = num/10
        	denom2 = denom%10
    	elif (num/10 == denom%10)and (denom%10 != 0):
        	num2 = num%10
        	denom2 = denom/10
   	 
    	if float(num)/float(denom) == float(num2)/float(denom2):
        	num_product *= num2
        	denom_product *= denom2
       	 
print num_product, "/", denom_product
