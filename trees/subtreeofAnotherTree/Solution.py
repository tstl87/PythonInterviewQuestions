class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, s, t):
        return self.traverse(s,t)
    
    def equals(self, s, t):
        if( not s and not t):
            return True
        if( not s or not t):
            return False
        return s.val==t.val and self.equals(s.left, t.left) and self.equals(s.right, t.right)
    
    def traverse(self, s, t):
        return (s is not None) and ( self.equals(s,t) or self.traverse(s.left, t) or self.traverse(s.right, t))
    
t3 = Node(4, Node(3), Node(2))
t2 = Node(5, Node(4), Node(-1))
t = Node(1, t2, t3)


s = Node(4, Node(3), Node(2))
"""
Tree t:
    1
   / \
  4   5 
 / \ / \
3  2 4 -1

Tree s:
  4 
 / \
3  2 
"""

print(Solution().isSubtree(t, s))
# True