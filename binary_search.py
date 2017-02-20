
def binary_search(sorted_vals, search_val): 
	# nums is a sorted set of values
	index = -1
	first = 0
	last = len(sorted_vals) - 1 
	while last > (first + 1):
		med = ((last-first)//2) + first
		med_val = sorted_vals[med]
		if med_val == search_val:
			return med
		if med_val < search_val:
			first = med
		else:
			last = med
	return index

nums = [5,10,15,20,32,34,65,75,88,99,101]
print (binary_search(nums, -1))
print (binary_search(nums, 65))