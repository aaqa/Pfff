m = []
while True:
	v = input()
	if v == 'end':
		break
	else:
		l = [int(x) for x in v.split()]
		m.append(l)

for j in range(len(m[0])):
	m[0][j] = 1
for i in range(len(m)):
	m[i][0] = 1

for i in range(1, len(m)):
	for j in range(1, len(m[0])):
		m[i][j] = m[i][j-1] + m[i-1][j]

for i in range(1, len(m)):
	for j in range(1, len(m[0])):
		print(m[i][j],end=' ')
	print()
