class linked_list:
	def __init__ (self, data = None):
		self.next = None
		self.data = data

	def append_to_tail(self, new_node_val):
		end = linked_list(new_node_val)
		temp = self
		while (temp.next is not None):
			temp = temp.next
		temp.next = end
	
	def print_contents(self):
		contents = []
		temp = self
		while temp is not None:
			contents.append(temp.data)
			temp = temp.next
		print (contents)

a = linked_list(5)
nums = [1,2,3,4,3,2,1,2]
for num in nums:
	a.append_to_tail(num)
a.print_contents()
