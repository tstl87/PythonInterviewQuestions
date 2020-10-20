class Solution:
    def climbStairs(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        anm2 = 1
        anm1 = 2
        for i in range(3,n+1):
            an = anm1 + anm2
            anm2 = anm1
            anm1 = an
            
        return an
    
    
print(Solution().climbStairs(10))