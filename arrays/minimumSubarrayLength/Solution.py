class Solution:
    def minSubArrayLen(self, s: int, nums):
        
        left = 0
        right = 0
        csum = 0
        rv = float('inf')
        
        while right < len(nums):
            csum += nums[right]
            while csum >= s:
                rv = min(rv, right - left + 1)
                csum -= nums[left]
                left += 1
            right += 1
        if rv == float('inf'):
            return 0
        else:
            return rv
        
print(Solution().minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
# 2