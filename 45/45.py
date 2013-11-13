from sets import Set

T = Set()
P = Set()
H = Set()

for n in range (1,100000):
	T.add(n*(n+1)/2)
	P.add(n*(3*n-1)/2)
	H.add(n*(2*n-1))

print T.intersection(P).intersection(H)
print "done"