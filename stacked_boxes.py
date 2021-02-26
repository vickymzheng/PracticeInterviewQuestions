'''
You have a stack of n boxes with widths w_i, height h_i, and depths d_i. 
The boxes cannot be rotated and can only be stacked on top of one another
if each box in the stack is strictly larger than the box above it in width,
height and depth. Implement a method to build the largest stack possible,
where the height of the stack is the sum of the heights each box in the stack
'''

class Box():
	def __init__(self, width, height, depth):
		self.width = width
		self.height = height
		self.depth = depth
	# returns true if self's dimensions are all less than other_box's
	def lessthan(self, other_box):
		return (self.width < other_box.width) and (self.height < other_box.height) and (self.depth < other_box.depth)

	# returns all the boxes that whose dimensions are less than self's
	def smaller_boxes(self, other_boxes):
		smaller_boxes = []
		for box in other_boxes:
			if box.lessthan(self):
				smaller_boxes.append(box)
		return smaller_boxes

def get_box_relationships(boxes):
	relationships = {}
	for box in boxes:
		relationships[box] = box.smaller_boxes(boxes)
	return relationships

def get_max_height(base_box, box_relationships, box_max_heights):
	if base_box in box_max_heights:
		return box_max_heights[base_box]

	max_stack = 0
	smaller_boxes = box_relationships[base_box]
	for box in smaller_boxes:
		max_box_height = get_max_height(box, box_relationships, box_max_heights)
		if max_box_height > max_stack:
			max_stack = max_box_height

	box_max_heights[base_box] = base_box.height + max_stack
	return box_max_heights[base_box]


def stacked_boxes(boxes):
	box_relationships = get_box_relationships(boxes)
	box_max_heights = {}
	max_stack_height = 0
	for box in boxes:
		stack_height = get_max_height(box, box_relationships, box_max_heights)
		if (stack_height > max_stack_height):
			max_stack_height = stack_height
	return max_stack_height


b1 = Box(1,1,1)
b2 = Box(2,2,2)
b3 = Box(3,3,3)

b4 = Box(1,0,1)
b5 = Box(5,2,2)
b6 = Box(3,9,2)
print(stacked_boxes([b6, b3, b1]))
