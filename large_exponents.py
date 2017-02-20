import math 
# calculate x^n where the value of x^n will exceed 2^32 and return the answer as a string
# This currently only works for single digit x

def large_multiply(value, x):
	v_len = len(value)
	add_extra = 0 
	print (value)
	for i in range(v_len-1, -1, -1):
		partial_prod = value[i] * x + add_extra
		if (partial_prod >= 10):
			value[i] = partial_prod%10
			add_extra = partial_prod//10
		else: 
			value[i] = partial_prod
			add_extra = 0

	#Append remaining overflow if necessary 
	if add_extra > 0:
		value = [add_extra] + value

	return value
def large_exponent(x, n):
	largest_exponent_in_mem = math.floor(32/(math.log(x)/math.log(2)))
	n = n - largest_exponent_in_mem
	value = str(x**largest_exponent_in_mem)
	value = [int(x) for x in list(value)]
	for i in range(0, n): 
		value = large_multiply(value, x)

	value = ''.join([str(x) for x in value])
	return value

print (large_exponent(9,14))