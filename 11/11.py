largest_product = 0;

input_file = open("data.txt")
;raw_data = input_file.read();
number_list = raw_data.split();

for current in range(0,len(number_list)):
	number_list[current] = int(number_list[current]);


for current in range(0,(len(number_list)-1)):

	current_col = (current + 1)%20;
	current_row = (current + 1)/20;
	
	if current_col < 16:
		product = number_list[current] * number_list[current + 1] * number_list[current + 2] * number_list[current + 3];
		if product > largest_product:
			largest_product = product;

	if current_row < 16:
		product = number_list[current] * number_list[current + 20] * number_list[current + 40] * number_list[current + 60];
		if product > largest_product:
			largest_product = product;

	if ((current_col < 16) and (current_row < 16)):
		product = number_list[current] * number_list[current + 21] * number_list[current + 42] * number_list[current + 63];
		if product > largest_product:
			largest_product = product
;
	if ((current_col > 3) and (current_row < 16)):
		product = number_list[current] * number_list[current - 19] * number_list[current - 38] * number_list[current - 57];
		if product > largest_product:
			largest_product = product;

print largest_product;