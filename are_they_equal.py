'''
Reverse to Make Equal
Given two arrays A and B of length N, determine if there is a way to make A equal to B by reversing any subarrays from array B any number of times.
Signature
bool areTheyEqual(int[] arr_a, int[] arr_b)
Input
All integers in array are in the range [0, 1,000,000,000].
Output
Return true if B can be made equal to A, return false otherwise.
Example
A = [1, 2, 3, 4]
B = [1, 4, 3, 2]
output = true
After reversing the subarray of B from indices 1 to 3, array B will equal array A.
'''

# to read: https://math.stackexchange.com/questions/3791053/generating-permutations-using-swaps-of-adjacent-elements
# since it is possible to generate all permutations just using swaps (aka reversing), if there is 
# the same characters in the same quantity then this is true
def val_count(vals):
	counts = {}
	for val in vals:
		if val not in counts:
			counts[val] = 0
		counts[val]+=1
	return counts
def are_they_equal(array_a, array_b):
	# Write your code here
	a_counts = val_count(array_a)
	b_counts = val_count(array_b)
	return a_counts == b_counts

a_1 = [1, 2, 3, 4]
b_1 = [1, 4, 3, 2]

a_2 = [1, 2, 3, 4]
b_2 = [1, 2, 3, 5] 

print(are_they_equal(a_1, b_1) == True)
print(are_they_equal(a_2, b_2) == False)