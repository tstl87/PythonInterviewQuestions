class Solution:
    def merge(self, intervals):
        def getFirst(elem):
            return elem[0]
        intervals.sort(key=getFirst)
        
        rv = []
        for interval in intervals:
            if not rv or rv[-1][1] < interval[0]:
                rv.append(interval)
            else:
                rv[-1][-1] = max(rv[-1][-1], interval[1])
            
        return rv
    
print(Solution().merge([[1, 5], [2, 8], [10, 12]]))
# [[1, 8], [10, 12]]