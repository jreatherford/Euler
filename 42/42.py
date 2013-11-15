size = 1000
triNumbers = [False] * size
index = 1
currTriangle = 1

while (currTriangle < size):
	triNumbers[currTriangle] = True
	index += 1
	currTriangle = int((index/2.0)*(index+1))

with open("words.txt") as file:
  word_list = file.read();

#prepare the file to be sorted
word_list = word_list.translate(None,"\"");
word_list = word_list.split(",")

total = 0
for word in word_list:
	word_score = 0
	for letter in word:
		word_score += ord(letter) - 64
	if (triNumbers[word_score]):
		total += 1

print total
