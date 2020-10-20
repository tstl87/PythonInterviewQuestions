class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:
    def invertTree(self, root):
        if root == None:
            return root
        else:
            right = self.invertTree(root.right)
            left = self.invertTree(root.left)
            root.right = left
            root.left = right
        return root
    
t = Node(4)
t.left = Node(2); t.right = Node(7)
t.left.left = Node(1); t.left.right = Node(3)
t.right.left = Node(6); t.right.right = Node(9)

print(Solution().invertTree(t))