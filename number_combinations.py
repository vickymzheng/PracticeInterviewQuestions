# Given a string of numbers on a number pad, enumerate all possible words

def create_numpad():
	numpad = {	'0' : [' '],
				'1' : [],
				'2': ['a', 'b', 'c'],
				'3': ['d', 'e', 'f'],
				'4': ['g', 'h', 'i'],
				'5': ['j', 'k', 'l'],
				'6': ['m', 'n', 'o'],
				'7': ['p', 'q', 'r', 's'],
				'8': ['t', 'u', 'v'],
				'9': ['w', 'x', 'y', 'z']}
	return numpad

numpad = create_numpad()

def build_string(nums, partial, ind, n):
	ans = []
	curr_num = nums[ind]
	while (curr_num == '1'):
		ind+=1 
		if (ind == n):
			return [partial]
		curr_num = nums[ind]
	letters = numpad[curr_num]
	if ((ind + 1) >= n):
		for letter in letters:
			ans.append(partial + letter)
	else:
		for letter in letters:
			ans+=build_string(nums, partial + letter, ind + 1, n)
	return ans

def pos_strings(nums):
	ans = []
	n = len(nums)
	ans = build_string(nums, '', 0, n)
	return ans
	
print(pos_strings('2222222'))
