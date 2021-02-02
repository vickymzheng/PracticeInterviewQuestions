#  Write a function to swap a number in place (without any temporary variables)
def swap(a, b):
	b = a * b
	a = b // a
	b = b // a 


a = 5
b = 10
swap(a,b)

def factorial(n):
	if n == 0 or n == 1:
		return 1
	return n * factorial(n-1)

# Write an algorithm to compute the number of trailing zeroes in n factorial
def trailing_zeroes_factorial(n):
	# get the number of things that multiple to something that is a factor of 10
	# if n <= 10, then it is two trailing zeroes from 2 * 5 and 10 
	# how many 2s and 5s does it consist of?
	# there will always be enough 2s 
	
	largest_pow_five = 1
	exponent = 1
	while (largest_pow_five < n):
		largest_pow_five*=5
		exponent+=1
	num_trailing_zeroes = 0
	pow_five = 5
	for i in range(1,exponent):
		num_trailing_zeroes+=(n // pow_five)
		pow_five*=5

	return num_trailing_zeroes
print(factorial(30))
print(trailing_zeroes_factorial(30)) # 7 (5, 10, 15, 20, 25, 30) (1, 1, 1, 1, 2, 1)
print(factorial(50))
print(trailing_zeroes_factorial(50)) # 12 (5, 10, 15, 20, 25, 30, 35, 40, 45, 50) (1, 1, 1, 1, 2, 1, 1, 1, 1, 2)
print(factorial(226))
print(trailing_zeroes_factorial(226)) 

