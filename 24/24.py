
def eu24 (target, list):
	permutations = 1;
	for n in range (1, len(list)+1):
		permutations *= n;

	return eu24helper(target, list, permutations);

def eu24helper(target, list, permutations):
	if (len(list) == 0):
		return "";

	cursor = 0;
	partition_size = permutations/len(list);
	while ( ((cursor + 1)*partition_size) < target):
		cursor += 1;

	target -= (cursor * partition_size);
	digit = list[cursor];

	permutations /= len(list);

	del list[cursor];

	return (str(digit) +  eu24helper(target, list, permutations))


list = range(10);
print eu24(1000000, list);