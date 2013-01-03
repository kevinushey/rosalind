from pandas import *

import os
os.chdir( "D:/dropbox/Dropbox/rosalind/lrep" )

dat = open("rosalind_lrep.txt").read().split('\n')[:-1]
s = dat[0]
k = dat[1]
edges = DataFrame([ x.split(' ') for x in dat[2:] ])
edges.columns = ['parent', 'child', 'loc', 'len']
edges.loc = edges.loc.map(int)
edges.len = edges.len.map(int)

## is the node an edge node?
edges['isEndNode'] = edges['loc'] + edges['len'] - 1 == len(s)

## how many children does a particular node have?
edges['numChildren'] = edges['isEndNode'].map(int)

def get_num_children(edges):

	for index, row in edges.iterrows():


def get_substring(edges):
	out = []
	for row in edges.iterrows():
		begin = int( row[1][2] ) - 1
		end = int( row[1][2] ) + int( row[1][3] ) - 1
		out.append( s[begin:end] )
	return out

print( get_substring(edges) )

def get_full_substring(edges):
	out = []
	for row in edges.iterrows():
		begin = int( row[1][2] ) - 1
		end = int( row[1][2] ) + int( row[1][3] ) - 1
		out.append( s[begin:] )
	return out

print( get_full_substring(edges) )

