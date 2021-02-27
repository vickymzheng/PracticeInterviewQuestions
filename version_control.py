# https://leetcode.com/problems/first-bad-version/
# [Y, Y, Y, N, N, N]
# [0, 1, 2, 3, 4, 5]
# Once there is a bug, it persists throughout the code
# Find the first instance of the bug
def first_bad_version(vers):
	n = len(vers)
	start = 0
	end = n - 1 
	while (start < end):
		mid = start + ((end - start) // 2)
		if vers[mid] == 'Y':
			start = mid + 1
		else:
			end = mid
	return start

Y = 'Y'
N = 'N'
ex1 = [Y, Y, Y, N, N, N]
ex2 = [Y, Y, Y, N, N]
ex3 = [Y, Y, N, N, N]

print(first_bad_version(ex1) == 3)
print(first_bad_version(ex2) == 3)
print(first_bad_version(ex3) == 2)