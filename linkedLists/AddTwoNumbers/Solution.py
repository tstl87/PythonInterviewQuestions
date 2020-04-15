class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        return self.addTwoNumbersRecursive(l1, l2, 0)
        #return self.addTwoNumbersIterative(l1, l2)

    def addTwoNumbersRecursive(self, l1, l2, c):
        val = l1.val + l2.val + c
        c = val // 10
        ret = Node(val % 10)

        if l1.next != None or l2.next != None:
            if not l1.next:
                l1.next = Node(0)
            if not l2.next:
                l2.next = Node(0)
            ret.next = self.addTwoNumbersRecursive(l1.next, l2.next, c)
        elif c:
            ret.next = Node(c)
        return ret

    def addTwoNumbersIterative(self, l1, l2):
        c = 0
        rv = current = None

        while l1 or l2:
            val = l1.val + l2.val + c
            c = val // 10
            if not current:
                rv = current = Node(val % 10)
            else:
                current.next = Node(val % 10)
                current = current.next

            if l1.next or l2.next:
                if not l1.next:
                    l1.next = Node(0)
                    if not l2.next:
                        l2.next = Node(0)
            elif c:
                current.next = Node(c)
            l1 = l1.next
            l2 = l2.next
        return rv

l1 = Node(2)
l1.next = Node(4)
l1.next.next = Node(3)

l2 = Node(5)
l2.next = Node(6)
l2.next.next = Node(4)

answer = Solution().addTwoNumbers(l1, l2)
while answer:
  print(answer.val, end=' ')
  answer = answer.next
# 7 0 8


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
