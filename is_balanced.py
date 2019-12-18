class tree_node: 
    def __init__(self, val = None, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
    
    def print_level(self, level):
        nodes_as_val = []
        for node in level:
            if (node is not None):
                nodes_as_val.append(node.val)
            else:
                nodes_as_val.append(None)
        print (nodes_as_val)
        
    def print_tree(self):
        if (self is None):
            print ("None")
            return 
        this_level = [self];
        nodes_added = 1
        while nodes_added > 0:
            nodes_added = 0
            self.print_level(this_level)
            next_level = []
            for node in this_level:
                if node is None:
                    next_level.append(None)
                    next_level.append(None)
                    continue
                if (node.left is not None):
                    nodes_added+=1
                if (node.right is not None):
                    nodes_added+=1
                next_level.append(node.left)
                next_level.append(node.right)
            this_level = next_level 

print("tree1")
node1 = tree_node(5)
node1.left = tree_node(3)
node1.right = tree_node(3)
node1.left.right = tree_node(2)
node1.right.left = tree_node(2)
node1.print_tree()

print("tree2")
node2 = tree_node(5)
node2.left = tree_node(3)
node2.right = tree_node(3)
node2.left.right = tree_node(2)
node2.right.left = tree_node(4)
node2.right.left.left = tree_node(4)
node2.print_tree()