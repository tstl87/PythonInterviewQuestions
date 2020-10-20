class Solution:
    def maxSubArray(self, nums):    
        rv = nums[0]
        currSum = 0
        
        for n in nums:
            if currSum + n < 0:
                currSum = 0
                rv = max(rv, n)
            else:
                currSum += n
                rv = max(rv,currSum)
                
        return rv
    
print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))