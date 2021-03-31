class Node():
  def __init__(self, val, left = None, right = None):
    self.val = val
    self.left = left
    self.right = right

class solution():
  def isValidBST(self, node):
    return self._isValidHelper(node, float('-inf'), float('inf'))

  def _isValidHelper(self, node, lower, upper):
    if not node:
      return True

    val = node.val
    if( (lower < val < upper) and 
      self._isValidHelper(node.left, lower, val) and 
      self._isValidHelper(node.right, val, upper) ):
      
      return True

    return False
    

    

#Example 1
#   5
#  / \
# 4   7
# solution: Truenode = Node(5)
node = Node(5)
node.left = Node(4)
node.right = Node(7)
print("Example 1 should be True: ", solution().isValidBST(node))

# Example 2
#   5
#  / \
# 4   7
#    /
#   2
# solution: False
node = Node(5)
node.left = Node(4)
node.right = Node(7)
node.right.left = Node(2)
print( "Example 2 should be False: ", solution().isValidBST(node) )
