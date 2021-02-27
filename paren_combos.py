# implement an algorithm to print all valid (e.g. properly opened and closed combinations of n paired paranthesis)
def paren_options(num_open, num_closed):
	options = []
	if num_open > 0:
		options.append('(')
	if num_closed > num_open:
		options.append(')')
	return options

def paren_combos(n):
	combos = []
	first_combo = {'combo' : '',
					'(' : n,
					')' : n}
	combos.append(first_combo)
	more_to_go = True
	while more_to_go:
		more_to_go = False
		new_combos = []
		for tup in combos:
			string = tup['combo']
			num_open = tup['(']
			num_closed = tup[')']
			options = paren_options(num_open, num_closed)
			for option in options:
				more_to_go = True
				new_combo = {'combo' : string + option,
								'(' : num_open,
								')' : num_closed}
				new_combo[option]-=1
				new_combos.append(new_combo)
		if (more_to_go):
			combos = new_combos

	for combo in combos:
		print(combo['combo'])

paren_combos(4)