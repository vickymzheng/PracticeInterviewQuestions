

# Given an m x n matrix where each value can be a color value, give the maximum size of adjacent squares with the same color
# https://www.youtube.com/watch?v=IWvbPIYQPFM
# Given a grid, find the maximum number of connected colors.

class Cord():
	def __init__(self, x, y, color):
		self.x = x
		self.y = y
		self.color = color
	def __repr__(self):
		return f'cord({self.x}, {self.y}, {self.color})'
	def __str__(self):
		return f'cord({self.x}, {self.y}, {self.color})'

	def __key(self):
		return (self.x, self.y, self.color)

	def __hash__(self):
		return hash(self.__key())

	def __eq__(self, other):
		if isinstance(other, Cord):
			return self.__key() == other.__key()
		return NotImplemented

def is_valid(x, y, m, n):
	return ((x >= 0) and (x < n)) and ((y >= 0) and (y < m))
 
def get_adjacent_cords(mat, cord):
	vert_neighbors = [-1, 1, 0, 0]
	hor_neighbors = [0, 0, -1, 1]
	n = len(mat)
	m = len(mat[0])
	color = cord.color
	neighbors = []
	for i in range(4):
		neighbor_x = cord.x + hor_neighbors[i]
		neighbor_y = cord.y + vert_neighbors[i]
		if (is_valid(neighbor_x, neighbor_y, m, n)):
			if mat[neighbor_x][neighbor_y] == color:
				neighbor = Cord(neighbor_x, neighbor_y, mat[neighbor_x][neighbor_y])
				neighbors.append(neighbor)
	return neighbors

def bfs(starting_node, graph):
	visited = set()
	queue = [starting_node]
	while len(queue) > 0:
		next_queue = []
		for node in queue:
			neighbors = graph[node]
			for neighbor in neighbors:
				if neighbor not in visited:
					next_queue.append(neighbor)
			visited.add(node)
		queue = next_queue
	return visited
def get_components(graph):
	components = {}
	visited = set()
	nodes = list(graph.keys())
	n = len(nodes)
	while (len(visited) < n):
		for node in nodes:
			if node not in visited:
				component_members = bfs(node, graph)
				visited = visited.union(component_members)
				components[node] = component_members
	return components

def make_graph(mat):
	n = len(mat)
	m = len(mat[0])
	graph = {}
	for i in range(n):
		for j in range(m):
			curr_cord = Cord(i, j, mat[i][j])
			graph[curr_cord] = get_adjacent_cords(mat, curr_cord)
	return graph

def max_connected_colors(mat):
	graph = make_graph(mat)
	components = get_components(graph)
	max_component_size = 0
	for component_id in components:
		component = components[component_id]
		num_component_members = len(component)
		if num_component_members > max_component_size:
			max_component_size = num_component_members
	return max_component_size

def print_mat(mat):
	for row in mat:
		print(row)

def print_graph(graph):
	for node in graph:
		line_to_print = str(node) + " : " + str(graph[node])
		print(line_to_print)


n = 3 # how many rows
m = 4 # how many columns 
mat = [['' for i in range(m)] for x in range(n)]
r = 'r'
g = 'g'
b = 'b'
mat[0][0] = g
mat[0][1] = g
mat[1][0] = g

mat[0][3] = r
mat[1][2] = r
mat[2][0] = r

mat[0][2] = b
mat[1][1] = b
mat[1][3] = b
mat[2][1] = b
mat[2][2] = b
mat[2][3] = b

print_mat(mat)
# print_graph(make_graph(mat))
print(max_connected_colors(mat))


