class Node():
  def __init__(self, value, left = None, right = None):
    self.value = value
    self.left = left
    self.right = right

class solution():
  def _isValidBSTHelper( self, node, lowerBound, upperBound):
    if( not node ):
      return True

    value = node.value
    if( lowerBound < value < upperBound 
      and self._isValidBSTHelper( node.left, lowerBound, value) 
      and self._isValidBSTHelper(node.right, value, upperBound) ):
      return True

    return False


  def isValidBST(self, n):
    return self._isValidBSTHelper( node, float('-inf'), float('inf'))


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
