def generate_reversals(x):
	out = []
	for i in range(0, len(x)-1):
		for j in range((i+1), len(x)):
			xx = x[:]
			xx[i:(j+1)] = xx[i:(j+1)][::-1]
			out.append( xx )
	return out

x = []