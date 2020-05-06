


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        import numpy as np
        if( m== 1 or n == 1 ):
            return 1
        
        m,n = max(m,n)-1, min(m,n)-1
        mn = m + n
        mf = 1
        nf = 1
        mnf = 1
        for i in range(mn):
            mnf *= i+1
            if( i+1 == m ):
                mf = int(mnf)
            if(i+1 == n ):
                nf = int(mnf)
        
        
        return int(mnf/(mf*nf))
    
    def uniquePaths2(self, m, n):
        matrix = []
        for i in range(m):
            matrix.append([0]*n)
        for i in range(m):
            matrix[i][0] = 1
        for j in range(n):
            matrix[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                matrix[i][j] = matrix[i][j-1] + matrix[i-1][j]
        return matrix[m-1][n-1]
    
    
print('Math approach: 3, 2')
print(Solution().uniquePaths(50,50))
print(' ')
print('CS approach: 3,2')
print(Solution().uniquePaths2(50,50))