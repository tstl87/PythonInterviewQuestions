# Defining a node
class Node():
  def __init__(self, val, next = None):
    self.val = val
    self.next = next

  def __str__(self):

    answer = ''
    n = self
    while n:
      answer += str(n.val) + ' '
      n = n.next

    return answer

class Solution():
  def reverse(self, node):

    prev = None
    curr = node
    while curr:
      temp = curr.next
      curr.next = prev
      prev = curr
      curr = temp

    return prev

node = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print(node)
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
 

            
        
        
        
