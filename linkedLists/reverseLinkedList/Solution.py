# Definition for singly-linked list.
class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None
        
    def __str__(self):
        result = str(self.val)
        if self.next:
            result += str(self.next)
        return result
    
class Solution:
    def reverseList(self,head):
        prev = None
        curr = head
        while(curr != None):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
    
    def reverseList2(self,head):
        if( head is None or head.next is None):
            return head
        
        p = self.reverseList2(head.next)
        head.next.next = head
        head.next = None
        return p
    
node = ListNode(1)
node.next = ListNode(2)
node.next.next = ListNode(3)
node.next.next.next = ListNode(4)
node.next.next.next.next = ListNode(5)

#print(Solution().reverseList(node))
print(Solution().reverseList2(node))

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
 

            
        
        
        
