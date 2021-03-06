#     5
#    / \
#   3   6
#    \   \
#     4   8
#          \
#           9
#            \
#             10
#              \
#               ...
#     5
#    / \
#   3   6
#    \
#     7
# 
def max_node_val(root, max_val = -1000):
    if (root is None): 
        return max_val
    if root.val > max_val:
        max_val = root.val 
    if root.left is not None:
        max_val = max_node_val(root.left, max(max_val, root.left.val))
    if root.right is not None:
        max_val = max_node_val (root.right, max(root.right.val, max_val))
    return max_val

def min_node_val(root, min_val = 1000):
    if root is None:
        return min_val
    if root.val < min_val:
        min_val = root.val 
    if root.left is not None:
        min_val = min_node_val(root.left, min(min_val, root.left.val))
    if root.right is not None:
        min_val = min_node_val (root.right, min(root.right.val, min_val))
    return min_val
    
def is_BST_n2(root, bst = True):
    # Max element to the left of the root has to be less than root
    # Min element to the right of the root has to be greater than equal to the root
    # if either of those conditions is violated, I would return False
    if root is None: 
        return True 
    if (bst is False):
        return False
    if root.left is not None: 
        bst = is_BST(root.left, (max_node_val(root.left) < root.val) and bst)
    if root.right is not None: 
        bst = is_BST(root.right, (min_node_val(root.right) >= root.val) and bst)
    print(str(root.val) + str(bst))
    return bst

def is_BST(root, upper_bound = 1000, lower_bound = -1000):
    if root is None: 
        return True 
    if (root.val > upper_bound) or (root.val < lower_bound):
        return False 
    bst = True
    if root.left is not None:
        bst = is_BST(root.left, root.val, lower_bound)
        if (bst is False):
            return False
    if root.right is not None: 
        bst = is_BST(root.right, upper_bound, root.val)
    return bst 

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

def size(curr_root):
    if (curr_root == None):
        return 0
    return 1+size(curr_root.left)+size(curr_root.right)

def nth_element(curr_root, n):
    if curr_root == None:
        return None
    left_sub_size = size(curr_root.left)
    if (left_sub_size == (n-1)):
        return curr_root.val
    if (left_sub_size >= n):
        return nth_element(curr_root.left,n)
    else:
        return nth_element(curr_root.right, n-(left_sub_size+1))


node = tree_node(5)
node.left = tree_node(3)
node.right = tree_node(6)
node.left.right = tree_node(4)

print (is_BST(node))
print(nth_element(node, 1))
print(nth_element(node,  2))
print(nth_element(node,  3))
print(nth_element(node,  4))