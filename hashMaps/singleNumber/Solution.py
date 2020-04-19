class Solution(object):
    def singleNumber(self, nums):
        occurrence = {}
        
        for n in nums:
            occurrence[n] = occurrence.get(n,0) + 1
        
        for key, value in occurrence.items():
            if value == 1:
                return key
            
    def singleNumber2(self, nums):
        unique = 0
        for n in nums:
            unique ^= n
            print(unique)
        return unique
    
print( Solution().singleNumber2([4,3,2,4,1,3,2]) )

# Hashmap Solution:
# Time Complexity:
# the time complexity is O(n) + O(n/2) so O(n) overall.

# Space Complexity:
# The hashmap we create is approximately O(n/2) so O(n) overall.

# XOR Solution:
# Time Complexity:
# the time complexity is O(n) for the single loop through the list

# Space Complexity:
# The space complexity is O(1) since we only create one new constant
# variable that we update.