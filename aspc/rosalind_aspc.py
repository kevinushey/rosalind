import math
import os

os.chdir("C:/Users/Kevin/Dropbox/rosalind/aspc")

def nCr(n,r):
	f = math.factorial
	return long( f(n) ) / long( f(r) ) / long( f(n-r) )

dat = open("rosalind_aspc.txt").read().rstrip("\n").split(" ")
n = long( dat[0] )
k = long( dat[1] )

x = 0L

for i in range(k, n+1):
	x += nCr(n, i)
	x = x % long(1E6)

print( x )