class Solution:
    def generateParetheses(self, n):
        res = []
        
        def backtrack(S, nleft, nright ):
            if len(S) == 2*n:
                res.append(S)
                return
            if nleft < n:
                backtrack(S+'(', nleft+1, nright)
            if nleft > nright:
                backtrack(S+')', nleft, nright+1)
        backtrack('',0,0)
        return res
    
print(Solution().generateParetheses(3))