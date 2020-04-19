class Solution:
    def reconstructQueue(self, people):
        # by making height negative, the tallest
        # people will be first since we sort order
        # is ascending.
        people.sort(key=lambda x: (-x[0],x[1])) # TC O(nlog_2(n))
        rv = []
        for p in people: # loop TC O(n)
            rv.insert(p[1],p) # sorted insert TC O(n)
        return rv
    
# Time Complexity:
# The loop with the sorted insert combined has a time
# complexity of O(n^2), which is the dominating term.

# Space Complexity:
# We created a vector of length n, so our space 
# complexity is O(n). 
    
    