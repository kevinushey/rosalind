import os

def count_breakpoints(x):
	xx = x[:]
	num_breakpoints = 0
	xx.insert( 0,min(x)-1 )
	xx.append( max(x)+1 )
	for i in range( len(x) - 1 ):
		if xx[i+1] == xx[i] + 1 or xx[i+1] == xx[i] - 1:
			continue
		else:
			num_breakpoints += 1

	return num_breakpoints

def generate_reversals(x):
	out = []
	for i in range(0, len(x)-1):
		for j in range((i+1), len(x)):
			xx = x[:]
			xx[i:(j+1)] = xx[i:(j+1)][::-1]
			out.append( xx )
	return out

def reversal_length(x, y):

	a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

	count = 0

	if x == y:
		print( "Already equal!" )
		return 0

	x = [y.index(xx)+1 for xx in x]

	visited_reversals = set()
	visited_reversals.add( tuple(x) )

	reversals = [x]

	while True:

		count += 1
		reversals = [ generate_reversals(xx) for xx in reversals ]
		reversals = sum( reversals, [] )
		reversals = [ xx for xx in reversals if tuple(xx) not in visited_reversals ]
		for xx in reversals:
			visited_reversals.add(tuple(xx))

		for xx in reversals:
			if xx == a:
				print( "Success at count = " + str(count) + "\n" )
				return( count )

		nbp = [count_breakpoints(xx) for xx in reversals]
		min_bp_index = [ index for index, value in enumerate(nbp) if value == min(nbp) ]

		reversals = [reversals[i] for i in min_bp_index]

		if count > 10:
			return( "Fail" )

os.chdir( "D:/dropbox/Dropbox/rosalind/rear")
data = open("rosalind_rear.txt").readlines()
data = [x.rstrip('\n') for x in data]

x_list = [ x.split(' ') for x in data[::3] ]
y_list = [ x.split(' ') for x in data[1::3] ]

for i in range( len( x_list ) ):
	print( reversal_length(x_list[i], y_list[i] ) )