# Write a function which returns true if the two specificed finary trees represent the same string, 
# and false otherwise. Note that two different shaped trees could have the same string representation


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
        this_level = [self]
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

def get_tree_string(t):
    if t == None:
        return ""
    if t.left == None and t.right == None:
        return t.val
    return get_tree_string(t.left) + get_tree_string(t.right)

def same_tree_string(t1, t2):
    return get_tree_string(t1) == get_tree_string(t2)


t1 = tree_node("N1")
t1.left = tree_node("N2")
t1.right = tree_node("N3")
t1.left.left = tree_node("Go")
t1.right.left = tree_node("og")
t1.right.right = tree_node("le!")

t2 = tree_node("N1")
t2.left = tree_node("Goo")
t2.right = tree_node("gle!")

t3 = tree_node("N1")
t3.left = tree_node("N2!")
t3.left.left = tree_node("Google")
t3.right = tree_node("!")

t4 = tree_node("N1")
t4.left = tree_node("N2")
t4.right = tree_node("N3")
t4.left.left = tree_node("Goog")
t4.left.right = tree_node("le")
t4.right.left = tree_node("!")

print(get_tree_string(t1))
print(get_tree_string(t2))
print(get_tree_string(t3))
print(get_tree_string(t4))

