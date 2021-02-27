# Write a function which returns true if the two specificed finary trees represent the same string, 
# and false otherwise. Note that two different shaped trees could have the same string representation


class tree_node: 
    def __init__(self, val = None, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
        self.visited = False
    
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

def is_leaf(node):
    if node == None:
        return False
    if node.left == None and node.right == None:
        return True

def get_all_leaves(s):
    while len(s) > 0:
        leaf = get_next_leaf(s)
        print(leaf)
# gets a stack of tree traversal 
def get_next_leaf(s):
    while (len(s) > 0 and s[-1].visited):
        s.pop()
    while (len(s) > 0 and not is_leaf(s[-1])):
        if s[-1].left != None and not s[-1].left.visited:
            s.append(s[-1].left)
        elif s[-1].right != None and not s[-1].right.visited:  
            s.append(s[-1].right)
        else: 
            s[-1].visited = True
            s.pop()

    if len(s) == 0:
        return ""

    s[-1].visited = True
    return s[-1].val

# what if the whole string can't fit into memory?
def same_tree_string_low_mem(t1, t2):
    if t1 == None and t2 == None:
        return True, "" 
    if t1 == None:
        return False 
    if t2 == None:
        return False 
    s1 = [t1]
    s2 = [t2]
    
    leaf1 = get_next_leaf(s1)
    leaf2 = get_next_leaf(s2)
    index1 = 0
    index2 = 0 
    while(len(s1) > 0 and len(s2) > 0):
        # print("")
        # print(f"leaf1: {leaf1}, leaf2: {leaf2}")
        # print(f"index1: {index1}, index2: {index2}")
        # print(f"leaf1[index1:]: {leaf1[index1:]}, leaf2[index2:]: {leaf2[index2:]}")
        # leaf2 is leaf1's prefix
        if leaf1[index1:].startswith(leaf2[index2:]) :
            # print("leaf2 prefix of leaf1 selected")
            index1 = index1 + (len(leaf2) - index2)
            index2 = 0 
            leaf2 = get_next_leaf(s2)
        # leaf1 is leaf2's prefix 
        elif leaf2[index2:].startswith(leaf1[index1:]) :
            # print("leaf1 prefix of leaf2 selected")
            index2 = index2 + (len(leaf1) - index1)
            index1 = 0 
            leaf1 = get_next_leaf(s1)
        else:
            # print("else selected")
            return False
    return (index1 == len(leaf1)) and (index2 == len(leaf2))

t1 = tree_node("N1")
t1.left = tree_node("N2")
t1.right = tree_node("N3")
t1.left.left = tree_node("Go")
t1.left.right = tree_node("")
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

t5 = tree_node("N1")
t5.left = tree_node("N2")
t5.right = tree_node("N3")
t5.left.left = tree_node("Go")
t5.right.left = tree_node("og")
t5.right.right = tree_node("le!")

t6 = tree_node("N1")
t6.left = tree_node("Goo")
t6.right = tree_node("gle!")

t7 = tree_node("N1")
t7.left = tree_node("N2")
t7.right = tree_node("N3")
t7.left.left = tree_node("Go")
t7.left.right = tree_node("")
t7.right.left = tree_node("og")
t7.right.right = tree_node("le!")

# print(get_tree_string(t1))
# print(get_tree_string(t2))
# print(get_tree_string(t3))
# print(get_tree_string(t4))

# can't do consecutive tests with the same trees because visited status gets updated in the function
print(same_tree_string_low_mem(t1, t5))
print(same_tree_string_low_mem(t7, t4))
# get_all_leaves([t1])



