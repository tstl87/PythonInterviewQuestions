class Solution(object):
  def twoSumA(self, nums, target):

    for i in range(len(nums)):
      for j in range(i+1, len(nums)):
        a, b = nums[i], nums[j]
        if a + b == target:
          return [i,j]

    return []

  def twoSumB(self, nums, target):

    diffs = {}
    for i in range( len(nums) ):
      diff = target - nums[i]
      if diff in diffs:
        return [diffs[diff], i]
      else:
        diffs[ nums[i] ] = i

    return []
    
print(Solution().twoSumB([2, 7, 11, 15], 18))