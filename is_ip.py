import sys 

def is_ip(number):
	number_length = len(number)
	if (number == ""):
		return False 
	if ((number[0] == "0") and (number_length > 1)):
		return False 
	val = int(number)
	return ((val < 256) and (val >= 0))

def all_valid_ips(number, nums_needed):
	valid_ips = set()
	ip_len = len(number)
	if (ip_len < nums_needed):
		return valid_ips

	if (nums_needed == 1):
		if is_ip(number):
			valid_ips.add(number)
		return valid_ips

	for i in range(3):
		a = number[:i+1]
		if (is_ip(a)):
			remaining_nums = number[i+1:]
			remaining_ips = all_valid_ips(remaining_nums, nums_needed-1)
			for remaining_ip in remaining_ips: 
				if (len(remaining_ips) > 0):
					valid_ip = a + "." + remaining_ip
					valid_ips.add(valid_ip)
		else:
			break 
	return valid_ips

def split_strings(some_str):
	str_len = len(some_str)
	for i in range(str_len-1):
		first_half = some_str[:i+1]
		second_half = some_str[i+1:]
		line_to_print = first_half + " " + second_half
		print(line_to_print)

query_num = sys.argv[1]
print(all_valid_ips(query_num, 4))
# split_strings(query_num)
