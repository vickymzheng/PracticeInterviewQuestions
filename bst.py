# 20170211 - Vicky's 3rd Interview Feedback: Check if a BT is a BST

# ---------------------------------------------------------------------------------------------------
# Score:
# ---------------------------------------------------------------------------------------------------
# [0.5/1 point] Explains strategy in a clear way to the interviewer before starting to code and confirms with interviewer if that makes sense and it is okay to code that initial solution (1 point)
#     - You explained your strategy of finding if there are violations in max_val in left subtree is smaller than root and min_val in right_substree is greater than root, but you didn't explain what happens after comparing just the root. You should have answered whether that's sufficient or if you are necessarily a BST at the root if you are a BST at the root.left and root.right?
# [0.0/1 point] Asks clarifying questions before jumping into code (ex. "Can we assume all inputs will be within a valid range or do we need to error handle?", "Is our function being used as an API endpoint or a part of a script in a data pipeline?", etc) (1 point)
#     - Should have asked what data the nodes hold instead of just assuming they're integers
#     - Good that you asked for the min and max values of the data the node should return (I told you -1000 to 1000 and all are integers)    
# [1.0/2 points] Gets at least a working solution down (2 points)
#     - Really close to getting a working solution
# [0.0/2 points] Gets the optimal solution (2 points)
# [1.0/1 point] Creates and runs adequate tests that ensure that the code written is correct (1 point)
#     - You thought of good test cases and covered a lot.
# [1.5/2 points] Explains the time complexity clearly and well (2 points)
#     - You initially thought O(N) but really this was O(N^2)
# [0.0/1 point] Explains the space complexity clearly and well (1 point)
#     - Never got to this point
# ---------------------------------------------------------------------------------------------------
# [5.0/10 points] total
# ---------------------------------------------------------------------------------------------------
# Comments:
# ---------------------------------------------------------------------------------------------------
# - Should know that Python classes are defined in camelCase and variables are underscore_case 
# - All functions that are related to a class should exist in the class (example: print_level should not be defined outside). If you don't want callers of the function to use it, append an underscore in front so that it's _print_level() and made private
# - You repeat a lot of work for every node looking through each node's entire subtree
# ---------------------------------------------------------------------------------------------------

# 45 minutes total, end at 3:24pm 

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
    
def is_BST(root, bst = True):
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


node = tree_node(5)
node.left = tree_node(3)
node.right = tree_node(6)
node.left.right = tree_node(4)
node.print_tree()
print (is_BST(node))