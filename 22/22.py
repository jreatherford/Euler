
def quickSort(list):
	if (len(list) <= 1):
		return list;

	pivot = list[0]

	less = [];
	greater = [];

	for n in list:
		if (n < pivot):
			less.append(n);
		elif (n > pivot):
			greater.append(n);

	return (quickSort(less) + [pivot] + quickSort(greater));

#---------------------------------------------------------------

def findScore (name, place):
	score = 0;
	for character in name:
		score+= (ord(character)-64)
	return score*place

#---------------------------------------------------------------

with open("names.txt") as file:
  names = file.read();

#prepare the file to be sorted
names = names.translate(None,"\"");
names = names.split(",")

names = quickSort(names);

grand_total = 0;

for current_name in range (0, len(names)):
	grand_total += findScore(names[current_name], current_name+1);

print grand_total;