class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        def length(head):
            if not head:
                return 0
            return 1 + length(head.next)
        
        lenA, lenB = length(headA), length(headB)
        currA, currB = headA, headB
        
        if lenA > lenB:
            for _ in range(lenA - lenB):
                currA = currA.next
        else:
            for _ in range(lenB - lenA):
                currB = currB.next
                
        while currA != currB:
            currA = currA.next
            currB = currB.next
            
        return currA
    
A = ListNode(3); A.next = ListNode(4); A.next.next = ListNode(5)
B = ListNode(1); B.next = ListNode(2); B.next.next = A

print(Solution().getIntersectionNode(A,B))
                