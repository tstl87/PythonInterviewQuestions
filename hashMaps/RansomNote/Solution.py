from collections import defaultdict

class Solution():
  def canSpell(self, magazine, note):
    letters = defaultdict(int)

    # n = len(magazine)
    # Time complexity O(n)
    for letter in magazine:
      letters[letter] += 1

    # m = len(note)
    # Time complexity O(m)
    for letter in note:
      if( letter not in letters or letters[letter] == 0):
        return False
      else:
        letters[letter] -= 1

    return True


print( Solution().canSpell(['a', 'b', 'c', 'd', 'e', 'f'], 'bed'))
# True

print( Solution().canSpell(['a', 'b', 'c', 'd', 'e', 'f'], 'cat'))
# False

# Time Complexity:
# If the magazine is a list of size m and the ransom is 
# a string of length n and we are looping through both of
# them once, then the time complexity is O(m) + O(n)

# Space Complexity:
# If the length of the magazine is of size m, then
# the Space Complexity comes from our hashmap and thus
# is O(m).

