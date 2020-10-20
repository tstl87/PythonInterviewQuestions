class Node:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next
	def __repr__(self):
		n = self
		ret = ''
		while n:
			ret += str(n.val) + ' '
			n = n.next
		return ret

class Solution:
	def removeZeroSumSublists1(self, head: Node) -> Node:
		hashMap, runningSum = {}, 0
		cur = head 
		while cur:
			runningSum += cur.val
			if runningSum == 0:
				head = cur.next
			else:
				if runningSum not in hashMap:
					hashMap[runningSum] = cur 
				else:
					hashMap[runningSum].next = cur.next
			cur = cur.next
		return head
	
# 3, 1, 2, -1, -2, 4, 1
n = Node(3)
n.next = Node(1)
n.next.next = Node(2)
n.next.next.next = Node(-1)
n.next.next.next.next = Node(-2)
n.next.next.next.next.next = Node(4)
n.next.next.next.next.next.next = Node(1)
print(Solution().removeZeroSumSublists(n))
# 3, 4, 1