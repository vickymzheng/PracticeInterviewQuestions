# given two strings, it will return the shorter and then longer one
def reorder(s1, s2):
	if len(s1) < len(s2):
		return s1, s2
	return s2, s1
# Return whether two strings are similar (i.e. one or fewer subst/ins/del)
def has_edit_dist_one(s1, s2):
	s1, s2 = reorder(s1, s2)
	n1 = len(s1)
	n2 = len(s2)
	if (n2 - n1) > 1:
		return False
	ind1 = 0
	ind2 = 0
	diff = 0
	while (ind1 < n1) and (ind2 < n2):
		if s1[ind1] != s2[ind2]:
			if (diff > 1):
				return False
			diff+=1
			if (n1 < n2):
				ind2+=1
			else:
				ind1+=1
				ind2+=1
		else:
			ind1+=1
			ind2+=1

	return (ind1 == n1) and (ind2 == n2)

s1 = 'caat'
s2 = 'bat'
print(has_edit_dist_one(s1, s2))