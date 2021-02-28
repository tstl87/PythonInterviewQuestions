class Node():
  def __init__(self, val, next = None):
    self.val = val 
    self.next = next 
  
  def __str__(self):

    n = self
    answer = ''
    while n:
      answer += str(n.val) + ' '
      n = n.next

    return answer

class Solution():
  def add(self, l1, l2):

    dummy = Node(0)
    result = dummy
    c = 0
    while( l1 or l2):

      # store current digit
      a, b = l1.val, l2.val
      dummy.val += (a + b + c) % 10
      print('a = ', a, 'b = ', b, 'a + b % 10 =', (a+b+c) % 10)
      c = (a + b + c) // 10

      if( l1.next and not l2.next ):
        l2.next = Node(0)

      if( not l1.next and l2.next ):
        l1.next = Node(0)

      l1, l2 = l1.next, l2.next

      if( l1 or l2):
        dummy.next = Node(0)
        dummy = dummy.next

      if( not ( l1 or l2 ) and c == 1):
        dummy.next = Node(c)

    return result

ll1 = Node(2, Node(4, Node(5)))
ll2 = Node(5, Node(6, Node(4)))

print(ll1)
print(ll2)
print( Solution().add(ll1,ll2), 'should be 7 0 8')

# Iterative Solution
# Time Complexity
# If l1 l1nd l2 are linked lists of size m l1nd n 
# respectively, then the time complexity is
# O(m+n)

# Space Complexity
# If l1 l1nd are linked lists of size m l1nd n 
# respectively, then the space complexity is
# l1lso O(m+n) 

# Recursive Solution:
# Time Complexity:

# Space Complexity:
