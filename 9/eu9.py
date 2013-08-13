import math

Squares = range (1,1000)

for i in range(0, len(Squares)):
	Squares[i] = Squares[i]**2


found = False;

for c in range ((len(Squares)-1)/3, len(Squares)-1, +1):
	a = 1
	b = c - 1

	while (b >= 0):

		if ((Squares[a] + Squares[b]) == Squares[c]):
			sqa = math.sqrt(Squares[a])
			sqb = math.sqrt(Squares[b])
			sqc = math.sqrt(Squares[c])
			if (sqa + sqb + sqc == 1000):
				print sqa*sqb*sqc
				found = True;
				break

		if found == True:
			break;

		a = a + 1
		if (a >= b):
			a = 1
			b = b - 1
