import os
import math

os.chdir("C:/Users/Kevin/Dropbox/rosalind/prob")

dat = open( "rosalind_prob.txt" ).read().split("\n")[:-1]
s = dat[0]
A = [ float(x) for x in dat[1].split(" ") ]
n = len(s)

n_GC = s.count("C") + s.count("G")
n_AT = len(s) - n_GC

out = [ math.log10( (x/2) ** n_GC * ((1-x)/2) ** n_AT ) for x in A ]
for item in out:
	print( round( item, 3 ) )