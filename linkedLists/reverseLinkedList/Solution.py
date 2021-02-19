# Defining a node
class Node:
  def __init__(self, value, next = None):
    self.value = value
    self.next = next 

  def __repr__(self):

    tmp = str(self.value)
    if self.next:
      tmp += ' ' + str(self.next)

    return tmp

# 1 ->  2   ->  3    -> 4        -> 5 ->
#               tmp  -> curr.next
#      prev <-  curr 
#      
#
class Solution:
  def reverse(self, node):

    curr = node
    prev = None
    while curr:
      tmp = curr.next
      curr.next = prev
      prev = curr
      curr = tmp

    return prev


node = Node(1, Node(2, Node(3, Node(4, Node(5)))))

print(Solution().reverse(node))
    

# Recursive Solution:
# Time Complexity:
# Since we loop through the linked list once, then the
# time complexity is O(n)

# Space Complexity:
# The cost of the recursive stack being called n-1 times
# is O(n)


#Iterative Solution:
# Time Complexity:
# Since we loop through the linked list once, then the
# time complexity is O(n)

# Space Complexity
# Since the additional space comes from defining and
# updating 3 new constant variables, then the space
# complexity is O(1)
 

            
        
        
        
