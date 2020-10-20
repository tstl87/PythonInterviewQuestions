class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0
        
        rv = 0
        m = prices[0]
        for p in prices:
            if p < m:
                m = p
            rv = max(rv, p - m)
        
        return rv
    
print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
# 5