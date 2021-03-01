# Given a bunch of users with unique integer user id’s, each with a vector<int> of friends and vector<int> of pages (pages they like), 
# find the pair of users with the maximum number of pages in common and who aren’t already friends.

class user():
	def __init__(self, user_id, friends, pages):
		self.user_id = user_id
		self.friends = friends
		self.pages = pages

def recommend_friend(users):
	page_users = {}
	
	# for each page, get the users that like it
	for user in users:
		for page in user.pages:
			if page not in page_users:
				page_users[page] = set()
			page_users[page].add(user.user_id)

	# for each user, get the people who like at least one of the same pages
	# as them and are not currently friends with them
	user_potential_friends = {}
	for user in users:
		current_friends = set(user.friends)
		current_friends.add(user.user_id)
		recommended_friends = set()
		for page in user.pages:
			potential_friends = page_users[page]
			recommended_friends = recommended_friends.union(potential_friends.difference(current_friends))
		user_potential_friends[user.user_id] = recommended_friends

	# for each user, get the pages they like
	liked_pages = {}
	for user in users:
		liked_pages[user.user_id] = set(user.pages)

	# for each user, count the number of pages they like with every 
	# user that is not their friend but likes a common page
	most_in_common = 0
	most_in_common_pair = ('user1', 'user2')
	for u1 in user_potential_friends:
		for u2 in user_potential_friends[u1]:
			u1_liked = liked_pages[u1]
			u2_liked = liked_pages[u2]
			num_common = len(u1_liked.intersection(u2_liked))
			if (num_common > most_in_common):
				most_in_common = num_common
				most_in_common_pair = (u1, u2)
	return most_in_common_pair 

user1 = user('user1', ['user2'], ['cats', 'dogs'])
user2 = user('user2', ['user1'], ['cats', 'dogs', 'fish'])
user3 = user('user3', [], ['cats', 'dogs', 'fish'])
test = [user1, user2, user3]
print(recommend_friend(test))	