
def collats (number, collats_dict):
	transitions = 0;
	previous_numbers = [];

	if (number == 1):
		collats_dict[1] = 0;

	while(number != 1):

		if (number in collats_dict):
			transitions += collats_dict[number];
			number = 1;

		else:
			transitions += 1;
			previous_numbers.append(number);

			if (number % 2 == 0):
				number = number/2;
			else:
				number = (3 * number) + 1;

	previous_numbers.reverse();
	while (len(previous_numbers) > 0):
		collats_dict[previous_numbers.pop()] = transitions;
		transitions -= 1;


longest_chain = 1;
max = 999999;
collat_list = {};

for current in range (1,max):
	if (current not in collat_list):
		collats(current,collat_list);

	if collat_list[current] > collat_list[longest_chain]:
		longest_chain = current;

print longest_chain;

