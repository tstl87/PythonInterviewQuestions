class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        return 1 + max( self.maxDepth(root.left), self.maxDepth(root.right))

    def maxDepth2(self, root):
        stack = []
        if root is not None:
            stack.append((1,root))
            
        depth = 0
        while stack != []:
            current_depth, root = stack.pop()
            if root is not None:
                depth = max(depth, current_depth)
                stack.append((current_depth+1, root.left))
                stack.append((current_depth+1, root.right))
        return depth
    
    
t = TreeNode(3)
t.left = TreeNode(9)
t.right = TreeNode(20)
t.right.left = TreeNode(15)
t.right.right = TreeNode(7)

print(Solution().maxDepth2(t))

print(Solution().maxDepth(t))