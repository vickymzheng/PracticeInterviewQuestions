'''
Say you overheard your friend’s password but don’t know how they spell it 
(e.g., if it is “password,” it could be spelled “pAsSwOrD,” “p455w0rD,” etc.).  
Given a word and a mapping from letters to characters (e.g., a maps to a, A, 4, @, etc.), 
print out all the possible passwords for that word.
'''

maps = { 'p' : ['P'],
		 'a' : ['A', '4', '@'],
		 's' : ['S', '5', 'z', 'Z'],
		 'w' : ['vv', 'W', 'VV'],
		 'o' : ['0', 'O'],
		 'r' : ['R'],
		 'd' : ['D'] }

# hp = head password
def all_possible_passwords(hp, maps):
	possible_passwords = set()
	possible_passwords.add(hp)
	n = len(hp)
	for i,val in enumerate(hp):
		pos_subs = maps[val]
		pos_starts = all_possible_passwords(hp[:i], maps)
		pos_ends = all_possible_passwords(hp[i+1:], maps)
		for sub in pos_subs:
			for start in pos_starts:
				for end in pos_ends:
					pos_pass = start + sub + end
					possible_passwords.add(pos_pass)
	return possible_passwords


password = 'password'
pos_passes = all_possible_passwords('password', maps)
for pos in pos_passes:
	print(pos)