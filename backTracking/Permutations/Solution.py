class Solution(object):
  def permute(self, nums, start=0):
    if start == len(nums)-1:
      return [nums.copy()] # equivalently could use return [nums[:]]
    
    result = []
    for i in range(start, len(nums)):
      nums[start], nums[i] = nums[i], nums[start]
      result += self.permute(nums, start+1)
      nums[start], nums[i] = nums[i], nums[start]
    
    return result



print(Solution().permute([1, 2, 3]))
# [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]]

#print(Solution().permute2([1, 2, 3]))
# [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]]

#print(Solution().permute2Iterative([1, 2, 3]))
# [[3, 2, 1], [3, 1, 2], [2, 3, 1], [2, 1, 3], [1, 3, 2], [1, 2, 3]]

# Time Complexity:
# Since we're looking for every permutation, then
# for a list of length n, our time complexity is O(n!)

# Space Complexity:
# Since we want to store every permutation of our list
# of length n, then our space complexity is O(n!).