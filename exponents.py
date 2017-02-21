def exponents(a,b):
	if b == 0:
		return 1
	if b == 1:
		return a 

	partial_product = 1
	if (b % 2 == 1):
		partial_product = exponents(a, (b-1)//2)
		return partial_product*partial_product*a 
	
	partial_product = exponents(a, (b)//2)
	return partial_product*partial_product

print(exponents(2,15))