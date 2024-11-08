import numpy as np
s1 =  18
s2 = 25
s3 = 40
k1 = []
k2 = []
k3 = []
c1 = 30
c2 = 50
c3 = 8
m = 0
f = []
b_count = 240


def u(s, k, c):
	return (c * np.sqrt(s/k)) / b_count 


def g(k):
	if k < 2:
		return 1
	if k >= 2:
		return -  0.5 * pow(k,2) + 3


def p(s):
	return 0.4 * s


for i in  range(1,40,4):
	i /= 10
	k1.append((i, u(s1, i, c1), s1))
	k2.append((i, u(s2, i, c2), s2))
	k3.append((i, u(s3, i, c3), s3))
for i in k1:
	for j in k2:
		for n in k3:
			if i[1] + j[1] + n[1] < 1:
				w_avg = (g(i[0]) + g(j[0]) + g(n[0])  + p(i[2]) + p(j[2]) + p(n[2]) ) / 3
				print( (p(i[2]) + p(j[2]) + p(n[2]) ) / 3)
				print(w_avg)
				if w_avg >  m:
					m = w_avg
					f = [(i[0], i[2], g(i[0])+p(i[2])), (j[0], j[2], g(j[0]) + p(j[2]) ) , (n[0], n[2],g(n[0]) + p(n[2]) ) ]
print((f,m))
