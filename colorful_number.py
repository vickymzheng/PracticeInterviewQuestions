def power_set(super_set, subsets):
	i = 1
	k = len(super_set)
	while (i <= k):
		for digit in super_set:
			super_set.remove(digit)
			power_set(super_set, subsets)
			subsets.add(super_set)
			super_set.add(digit)
	print(subsets)

def is_colorful(num):
	super_set = set()
	products = set()
	total_prod = 1;
	while(num > 0):
		digit = num % 10 
		num = num / 10
		if (digit in super_set):
			return False
		super_set.add(digit)
		total_prod = total_prod * digit

	subsets = set()
	power_set(super_set,subsets)


is_colorful(1245)