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

def store(root):
    if root == None:
        return []
    to_process = []
    to_process.append([root, 0])
    nums = []
    pos = []
    while (len(to_process) > 0):
        curr_node = to_process.pop(0)
        node_id = curr_node[0]
        nums.append(node_id.val)
        ind = curr_node[1]
        pos.append(ind)
        if (node_id.left):
            to_process.append([node_id.left, ind * 2 + 1])
        if (node_id.right):
            to_process.append([node_id.right, ind * 2 + 2])
    return nums + pos

def restore(tree_info):
    n = len(tree_info)
    if (n == 0):
        return None
    nums = tree_info[:n/2]
    pos = tree_info[n/2:]
    
    root = tree_node(nums[0])
    if (n == 2): 
        return root 

    parent_ind = 0
    curr_node = root
    to_process = [root]

    child_ind = 1
    n = n / 2
    while (child_ind < n):
        tree_parent_ind = pos[parent_ind]
        left = tree_parent_ind * 2 + 1
        right = tree_parent_ind * 2 + 2
        tree_child_ind = pos[child_ind]
        if tree_child_ind == left or tree_child_ind == right:
            new_node = tree_node(nums[child_ind])
            if tree_child_ind == left:
                curr_node.left = new_node
            else:
                curr_node.right = new_node
            child_ind+=1
            to_process.append(new_node)
        else:
            parent_ind+=1 
            to_process.pop(0)
            curr_node = to_process[0]
    return root


node = tree_node(5)
node.left = tree_node(3)
node.right = tree_node(6)
node.left.right = tree_node(4)
node.print_tree()
# print(nth_element(node, 1))
# print(nth_element(node,  2))
# print(nth_element(node,  3))
# print(nth_element(node,  4))
# print(store(node))
reconstructed_tree = restore(store(node))
print("Reconstructed tree: ")
reconstructed_tree.print_tree()
# print(nth_element(reconstructed_tree, 1))
# print(nth_element(reconstructed_tree,  2))
# print(nth_element(reconstructed_tree,  3))
# print(nth_element(reconstructed_tree,  4))