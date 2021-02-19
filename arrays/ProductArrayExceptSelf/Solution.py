class Solution:
  def productExceptSelf(self, nums):

    # initialize results array as a starting product of ones
    res = [1]*len(nums)

    # forward pass computing products for the next entry 
    prod = 1
    for i in range(0,len(nums)-1):
      prod *= nums[i]
      res[i+1] *= prod

    # backward pass computing products for the next entry
    prod = 1
    for i in range(-1, -len(nums), -1):
      prod *= nums[i]
      res[i-1] *= prod

    return res

print(Solution().productExceptSelf([1, 2, 3, 4]))
# [24, 12, 8, 6]