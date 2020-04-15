class Solution:
    def permute(self, nums):
        result = []
        
        def permuteHelper(start):
            if start == len(nums)-1:
                result.append(nums[:])
            
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                permuteHelper(start+1)
                nums[start], nums[i] = nums[i], nums[start]
        permuteHelper(0)
        return result 
    
    
print(Solution().permute([1,2,3]))

# Time Complexity:
# Since we're looking for every permutation, then
# for a list of length n, our time complexity is O(n)

# Space Complexity:
# Since we want to store every permutation of our list
# of length n, then our space complexity is O(n).
            