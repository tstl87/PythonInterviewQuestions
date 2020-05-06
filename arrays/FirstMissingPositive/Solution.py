class Solution:
    def firstMissingPositive(self, nums):
        
        nums = set(nums)
        n = len(nums)
        
        for i in range(1,n+2):
            if i not in nums:
                return i
            

print('[]')            
print(Solution().firstMissingPositive([]))
print('')

print('[1]')            
print(Solution().firstMissingPositive([1]))
print('')

print('[4,-1,1,3]')            
print(Solution().firstMissingPositive([4,-1,1,3]))
print('')
