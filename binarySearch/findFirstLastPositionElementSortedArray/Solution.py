class Solution:
  def getRange(self, arr, target):
    return self.binarySearchIterative(arr)
  def binarySearchIterative(self, array, target):
    


arr = [1, 3, 3, 5, 7, 8, 9, 9, 9, 15]
print(Solution().getRange(arr, 9))
# [6, 8]

# Iterative Solution:
# Time Complexity:
# Binary search algorithm on an ordered list of length n
# has a time complexity of O(log_2(n))

# Space Complexity:
# We are only creating and updating two variables so
# our space complexity is O(1)

# Recursive Soluition:
# Time Complexity:
# Binary search algorithm on an ordered list of length n
# has a time complexity of O(log_2(n))

# Space Complexity:
# Since we are using recursion, there is a Recusion cost
# that matches our time complexity cost of O(log_2(n)).