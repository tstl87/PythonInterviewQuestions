# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isUnivalTree(self, root):
        def dfs(node):
            return not node or node.val == root.val and dfs(node.left) and dfs(node.right)
        return dfs(root)
                
            
t1 = TreeNode(1); t1.left = TreeNode(1); t1.right = TreeNode(1)
t1.left.left = TreeNode(1); t1.left.right = TreeNode(1)
t1.right.right = TreeNode(1)

t2 = TreeNode(2); t2.left = TreeNode(2); t2.right = TreeNode(2)
t2.left.left = TreeNode(4); t2.left.right = TreeNode(2)
t2.right.right = TreeNode(2)


print( Solution().isUnivalTree(t1))

print( Solution().isUnivalTree(t2))