#  Write a function to swap a number in place (without any temporary variables)
def swap(a, b):
	b = a * b
	a = b // a
	b = b // a 


a = 5
b = 10
swap(a,b)

# Write an algorithm to compute the number of trailing zeroes in n factorial
def factorial(n):
	if n == 0 or n == 1:
		return 1
	return n * factorial(n-1)

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

# print(factorial(30))
print(trailing_zeroes_factorial(30)) # 7 (5, 10, 15, 20, 25, 30) (1, 1, 1, 1, 2, 1)
# print(factorial(50))
print(trailing_zeroes_factorial(50)) # 12 (5, 10, 15, 20, 25, 30, 35, 40, 45, 50) (1, 1, 1, 1, 2, 1, 1, 1, 1, 2)
# print(factorial(226))
print(trailing_zeroes_factorial(226)) # 55

# A child is running up a staircase with n steps and can either hop 1, 2 or 3 steps at a time. 
# Implement a function to count the number of ways a child can run up the stairs
# 4 : 1, 1, 1, 1 or 1, 1, 2 or 1, 2, 1 or 2, 1, 1 or 2,2 or 1,3 or 3,1 = 7 ways 
# number of unique ways to get from 4 should be equal to number of unique ways to traverse two steps times number of unique ways to traverse two steps
# minus duplicates? i.e 1, 1
def unique_steps(n):
	if n < 1:
		return 0
	if n == 1:
		return 1
	# 1,1 or 2
	if (n == 2):
		return 3
	# 1, 1, 1 or 1, 2 or 2,1 or 3
	if (n == 3):
		return 4
	
	num_unique_steps = unique_steps(n-3)
	num_unique_steps+= unique_steps(n-2)
	num_unique_steps+= unique_steps(n-1)
