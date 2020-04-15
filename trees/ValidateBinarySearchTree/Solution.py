# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root):
        def helper(node, left, right):
            # if empty, return true
            if not node:
                return True
    
            val = node.val
            # check that node is between children
            if val <= left or val >= right:
                return False
            
            # check if right node tree obeys values.
            if not helper(node.right, val, right):
                return False
            
            # check if left node obeys tree values.
            if not helper(node.left, left, right):
                return False
            
            # Everything passed, return True
            return True
        return helper(root, float('-inf'), float('inf'))

# Time complexity:
# Since we check each node once in our recursion and
# if we assume that there are n nodes, then the time
# complexity is O(n)

# Space complexity:
# There is no additional data used other than the 
# method variables and the return value, so indeed, 
# all memory is "cost of recursion". In this case
# The cost comes from updating the upper or lower 
# bound. The the total cost would hence be  
# linearly proportional to the depth of the tree.

# In a balanced binary search tree, the depth is 
# O(log n), so indeed, the space complexity would 
# be O(log n) too. However, in general a BST is 
# not necessarily balanced, it could even be a 
# chain of length n, if the root is the minimum, 
# its right child is the second smallest element, 
# and so on. In that case the space complexity 
# of this recursion is O(n).

node = TreeNode(5)
node.left = TreeNode(4)
node.right = TreeNode(7)

node.left.left = TreeNode(1)
node.left.right = TreeNode(4.5)

node.right.left = TreeNode(6)
node.right.right = TreeNode(8)

print(Solution().isValidBST(node))