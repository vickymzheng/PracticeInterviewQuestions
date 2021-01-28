from math import inf 

# min heap, will store key value pairs
# the thing with the value has the highest priority
class priority_queue:
	storage = []

	# returns true key of kv1 is less than key of kv2
	def lessthan(self,kv1, kv2):
		return kv1[1] < kv2[1]

	def swap(self,ind1, ind2):
		holder = self.storage[ind1]
		self.storage[ind1] = self.storage[ind2]
		self.storage[ind2] = holder

	def add(self, kv):
		self.storage.append(kv)
		child = self.size() - 1
		parent = child // 2
		while (self.lessthan(self.storage[child], self.storage[parent])):
			self.swap(child, parent)
			child = parent
			parent = child // 2

	def pop(self):
		if (len(self.storage) <= 1):
			self.storage = []
			return
		self.storage[0] = self.storage[-1]
		self.storage.pop(-1)
		parent = 0
		bubble_down = True
		while (bubble_down):
			left = parent * 2 + 1
			right = parent * 2 + 2
			left_val = (inf, inf)
			right_val = (inf, inf)
			if (left < self.size()):
				left_val = self.storage[left]
			if (right < self.size()):
				right_val = self.storage[right]
			min_ind = left
			min_val = left_val
			if (self.lessthan(right_val, left_val)):
				min_ind = right
				min_val = right_val
			if (self.lessthan(min_val, self.storage[parent])):
				self.swap(min_ind, parent)
				parent = min_ind
			else:
				break

	def top(self):
		return self.storage[0]
	
	def size(self):
		return len(self.storage)

	def empty(self):
		return self.size() == 0
	
	def show(self):
		print(self.storage) 

def dijkstra(g, s, t):
	n = len(g)
	node_dists = [inf]*n
	node_dists[s] = 0
	nodes = list(range(n)) 
	current = s
	visited = [0] * n
	visited[current] = 1
	pq = priority_queue()
	pq.add((s,0))
	while (sum(visited) < n):
		current = pq.top()
		node = current[0]
		dist = current[1]
		visited[node] = 1
		pq.pop()
		neighbors = g[node]
		for i,neigh_dist in enumerate(neighbors):
			new_pos_dist = dist + neigh_dist
			if new_pos_dist < node_dists[i]:
				node_dists[i] = new_pos_dist
			if visited[i] == 0:
				pq.add((i, node_dists[i]))
	return node_dists[t]

	
	

g1 = [[0, 2, 2, 2, -1], 
	  [9, 0, 2, 2, -1], 
	  [9, 3, 0, 2, -1], 
	  [9, 3, 2, 0, -1], 
	  [9, 3, 2, 2, 0]]

g2 = [[0, 1, 1, 1, 1], 
	  [1, 0, 1, 1, 1], 
	  [1, 1, 0, 1, 1], 
	  [1, 1, 1, 0, 1], 
	  [1, 1, 1, 1, 0]]

g3 = [[0, 1, 5],
	  [0, 0, 1],
	  [0, 0, 0]]


print(dijkstra(g3, 0, 2))