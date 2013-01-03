from ete2 import Tree
import os
import re

def has_names(x):
	if re.match("\)[a-zA-Z]", x) is not None:
		return True
	else:
		return False

os.chdir("/Users/kevinushey/Dropbox/rosalind/nwck")
dat = open("rosalind_nwck.txt").read().split("\n")

tree_indices = list( range(0, len(dat)-1, 3) )
tree_paths = list( range(1, len(dat)-1, 3) )

trees = [dat[i][:] for i in tree_indices]

paths = [dat[i][:] for i in tree_paths]

dat = []
for i in range( len( trees ) ):

	if has_names( trees[i] ):
		flag = 8
	else:
		flag = 9

	dat.append({
		"tree": Tree( trees[i], flag ),
		"paths": paths[i].split(" ")
	})

outFile = open("rosalind_out.txt", 'w')

for item in dat:

	## tree
	tree = item["tree"]

	## get the nodes
	node1 = item["paths"][0]
	node2 = item["paths"][1]

	outFile.write( str( int( tree.get_distance(node1, node2) ) ) )
	outFile.write( " " )

outFile.close()