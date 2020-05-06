# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __str__(self):
        c = self
        answer = ''
        while c:
            answer += str(c.val) if c.val else ""
            c = c.next
        return answer
    
class Solution:
    def mergeKLists(self, lists):
        head = temp = ListNode(-1)
        
        while any(list is not None for list in lists):
            temp_min, i  = min( (list.val, i) for i, list in enumerate(lists) if list is not None)
            lists[i] = lists[i].next
            temp.next = ListNode(temp_min)
            temp = temp.next
            
        return head.next
    
a = ListNode(1, ListNode(3, ListNode(5)))
b = ListNode(2, ListNode(4, ListNode(6)))

print(a)
# 135
print(b)
# 246
print(Solution().mergeKLists([a, b]))
# 123456