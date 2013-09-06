with open("67.txt") as file:
	tree = file.readlines();

for current_row in range (len(tree)):
	tree[current_row] = tree[current_row].split();

for row in range (len(tree)-2, -1, -1):
	for node in range (len(tree[row])-1, -1, -1):

		left = tree[row+1][node];
		right = tree[row+1][node+1];

		if (int(left) > int(right)):
			tree[row][node] = int(left) + int(tree[row][node]);
		else:
			tree[row][node] = int(right) + int(tree[row][node]);

print tree[0][0];