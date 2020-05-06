class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        curr = dummy = ListNode(0)
        dummy.next = head
        prefix = 0
        from collections import OrderedDict
        seen = OrderedDict()
        while curr:
            prefix += curr.val
            if prefix not in seen:
                seen[prefix] = curr
            else:
                node = seen[prefix]
                node.next = curr.next
                while list(seen.keys())[-1] != prefix:
                    seen.popitem()
            curr = curr.next
        return dummy.next
    

ex1 = ListNode(1); ex1.next = ListNode(2); ex1.next = ListNode(-3);
ex1.next = ListNode(3); ex1.next = ListNode(1)
#[1,2,-3,3,1]

print( Solution().removeZeroSumSublists(ex1))