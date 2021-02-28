import heapq

class Solution():
  def findKthLargest1(self, nums, k):
    nums = sorted(nums)
    return nums[-k]

  def findKthLargest2(self, nums, k):
    return heapq.nlargest(k,nums)[-1]


print('[3,2,3,1,2,4,5,5,6] and k = 4')
print( Solution().findKthLargest2([3,2,3,1,2,4,5,5,6],4) )
print('')
print('[3,2,1,5,6,4] and k=2')
print( Solution().findKthLargest2( [3,2,1,5,6,4], 2 ) )