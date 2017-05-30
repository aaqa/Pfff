a = [int(x) for x in input().split()]

def fact(n):
	if n == 1:
		return 1
	else:
		return n * fact(n)

for x in a:
	print(fact(x))


