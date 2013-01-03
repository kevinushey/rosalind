import os
from Bio import SeqIO

os.chdir("C:/Users/Kevin/Dropbox/rosalind/trans")

def read_FASTA( file ):
	handle = open( file, "rU" )
	return list(SeqIO.parse(handle, "fasta"))

strings = read_FASTA("rosalind_trans.txt")

s1 = strings[0].seq.tostring()
s2 = strings[1].seq.tostring()

n_transitions = 0 ## A <-> G
n_transversions = 0 ## C <-> T

purines = ["A", "G"]
pyrimidines = ["C", "T"]

for i in range( len(s1) ):

	if s1[i] != s2[i]:

		if s1[i] in purines and s2[i] in purines or s1[i] in pyrimidines and s2[i] in pyrimidines:
			n_transitions += 1

		if s1[i] in purines and s2[i] in pyrimidines or s1[i] in pyrimidines and s2[i] in purines:
			n_transversions += 1

print( float(n_transitions) / float(n_transversions) )