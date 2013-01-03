def factorial(x):
	if x == 0:
		return 1
	else:
		return x * factorial(x-1)

print( factorial(20) )

def factorial2(x):
	def factorialIter(x, acc):
		if x == 0:
			return acc
		else:
			return factorialIter(x-1, acc*x)

	return factorialIter(x, 1)



print( factorial2(100) )