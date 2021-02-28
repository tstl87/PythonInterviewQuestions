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
  def remove_kth_from_linked_list(self, ll, k):

    slow, fast = ll, ll
    for _ in range(k):
      fast = fast.next

    head = slow
    prev = None
    while fast:
      prev = slow
      slow = slow.next
      fast = fast.next
    prev.next = slow.next

    return head

    

head = Node(1, Node(2, Node(3, Node(4, Node(5, None)))))
#print(head)
# 12345

head = Solution().remove_kth_from_linked_list(head, 2)
print(head)
# 1235