class Solution:
  def threeSumBruteForce(self, nums):

    rv = []
    for i in range(len(nums)):
      for j in range(i+1, len(nums)):
        for k in range(j+1, len(nums)):
          a, b, c = nums[i], nums[j], nums[k]
          if a + b + c == 0:
            rv += [[a,b,c]]

    return rv

  def threeSumHashmap(self, nums):

    nums.sort()
    rv = []
    for i in range( len(nums)):
      self.twoSumHashmap(nums, i, rv)

    return rv

  def twoSumHashmap(self, nums, start, results):

    dic = {}
    target = -nums[start]
    for i in range( start+1, len(nums)):
      n = nums[i]
      diff = target - n
      if diff in dic:
        return results.append([n, diff, -target])
      dic[n] = 1

  def threeSumIndices(self, nums):

    result = []
    for i in range( len(nums) ):
      twoSumIndices
    return result




print(Solution().threeSumBruteForce([-1, 0, 1, 2, -4, -3]))
# [[-1, 0, 1], [1, 2, -3]]

print(Solution().threeSumHashmap([-1, 0, 1, 2, -4, -3]))
#[[2, 1, -3], [1, 0, -1]]

#print(Solution().threeSumIndices([-1, 0, 1, 2, -4, -3]))
# [[-3, 1, 2], [-1, 0, 1]]