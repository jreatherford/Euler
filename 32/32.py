
def isPanDigital (digits):
	if (len(digits) != 9):
		return False

	if not "1" in digits: return False
	if not "2" in digits: return False
	if not "3" in digits: return False
	if not "4" in digits: return False
	if not "5" in digits: return False
	if not "6" in digits: return False
	if not "7" in digits: return False
	if not "8" in digits: return False
	if not "9" in digits: return False

	return True

product_list = []

for x in range (100,10000):
	for y in range (1,x+1):

		product = (x*y)
		digits = str(x) + str(y) + str(product);

		if (len(digits) > 9):
			break

		if (isPanDigital(digits) == True):
			product_list.append(product)

total = 0;
product_list = set(product_list)

for i in product_list:
	total += i;

print total