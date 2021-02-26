class cord():
	def __init__(self, x, y):
		self.x = x
		self.y = y
	def __repr__(self):
		return f'cord({self.x}, {self.y})'
	def __str__(self):
		return f'cord({self.x}, {self.y})'

def copy_matrix(mat):
	new_mat = []
	for i,row in enumerate(mat):
		new_mat.append([])
		for j,col in enumerate(mat[i]):
			new_mat[i].append(col)
	return new_mat

def is_diagonal(pos1, pos2):
	x_dif = pos1.x - pos2.x
	y_dif = pos1.y - pos2.y
	return abs(x_dif) == abs(y_dif)

def crosses_paths(pos1, pos2):
	return (pos1.x == pos2.x) or (pos1.y == pos2.y) or is_diagonal(pos1, pos2)

def queen_points(queen_positions, visited, n):
	if (len(queen_positions) == n):
		return [queen_positions]

	last_pos = queen_positions[-1]
	start_x = last_pos.x
	start_y = last_pos.y
	all_combos = []
	for i in range(n):
		for j in range(n):
			if (i < start_x and j < start_y):
				continue
			curr_pos = cord(i, j)
			if (not visited[i][j]):
				compatible = True
				for prev_pos in queen_positions:
					if crosses_paths(prev_pos, curr_pos):
						compatible = False
						break
				if (compatible):
					visited[i][j] = True
					combos = queen_points(queen_positions + [curr_pos], copy_matrix(visited), n)
					for combo in combos:
						if len(combo) > 0:
							all_combos.append(combo)
	return all_combos

def get_all_queen_pos(n = 8):
	board = [[False]*n for x in range(n)]
	all_combos = []
	for i in range(n):
		for j in range(n):
			if not board[i][j]:
				starting_point = cord(i, j)
				visited = [[False]*n for x in range(n)]
				combos = queen_points([starting_point], visited, n)
				all_combos+=combos
				for combo in combos:
					for point in combo:
						board[point.x][point.y] = True

	for combo in all_combos:
		print(combo)

get_all_queen_pos()
