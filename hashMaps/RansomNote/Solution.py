from collections import defaultdict

class Solution(object):
	def canSpell(self, magazine, note):
		letters = defaultdict(int)
		for c in magazine:
			letters[c] += 1

		for c in note:
			if letters[c] <= 0:
				return False
			letters[c] -= 1

		return True

print(Solution().canSpell(['a', 'b', 'c', 'd', 'e', 'f'], 'bed'))
# True

print(Solution().canSpell(['a', 'b', 'c', 'd', 'e', 'f'], 'cat'))
# False

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

