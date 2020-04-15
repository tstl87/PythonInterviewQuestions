class Solution:
    def canConstruct(self, ransomNote, magazine):
        mag_dict = {}
        for char in magazine:
            if(char in mag_dict.keys()):
                mag_dict[char] += 1
            else:
                mag_dict[char] = 1
        for char in ransomNote:
            if(char in mag_dict.keys()):
                mag_dict[char] -= 1
                if mag_dict[char] < 0:
                    return False
            else:
                return False
        return True

# Time Complexity:
# If the magazine is a list of size m and the ransom is 
# a string of length n and we are looping through both of
# them once, then the time complexity is O(m) + O(n)

# Space Complexity:
# If the length of the magazine is of size m, then
# the Space Complexity comes from our hashmap and thus
# is O(m).
    
# Space Complexity:
print(Solution().canConstruct('aa', 'aab'))

