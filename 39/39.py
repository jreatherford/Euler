import math
size = 1000
p_set = [0] * (size+1)
for a in range (1,size + 1):
	for b in range (1,size + 1):
		if (a+b) > size:
			break
		c = math.sqrt(a**2 + b**2)
		if (((a + b + c) < size) and (c.is_integer())):
			c = int(c)
			p_set[(a+b+c)] += 1

max_p = 0;
max_size = 0;
for p in range(1,size+1):
	if p_set[p] > max_size:
		max_size = p_set[p]
		max_p = p

print max_p