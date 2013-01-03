import math

def nCr(n,r):
	f = math.factorial
	return long( f(n) ) / long( f(r) ) / long( f(n-r) )

n = 1702L
k = 1279L

x = 0L

for i in range(k, n+1):
	x += nCr(n, i)
	x = x % long(1E6)

print( x )