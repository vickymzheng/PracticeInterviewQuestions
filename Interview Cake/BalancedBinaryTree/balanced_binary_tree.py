  class BinaryTreeNode:

    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right

def is_balanced(tree_root):
    depths = [] 
    nodes = [] 
    nodes.append((tree_root, 0))
    while len(nodes):
        node, depth = nodes.pop() 

        if (not node.left) and (not node.right) :
        #we found a leaf
            if depth not in depths:
                depths.append(depth)
                if (len(depths) > 2) or abs(depths[0] - depths[1]) > 1): 
                    return False

        else:
            if node.left:
                nodes.append(node.left)
            if node.right: 
                nodes.append(node.right)
    return True; 