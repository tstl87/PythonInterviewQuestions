class Solution:
    def numIslands(self, grid):
        # initialize variables
        if not grid:
            return 0
        
        islandCount = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    islandCount += 1
                    self._numIslandsHelper(i,j, grid)
                    
        return islandCount

    def _numIslandsHelper(self, i, j, grid):
        
        if(i == -1 or i == len(grid) or j == -1 or j == len(grid[0]) or grid[i][j] != "1"):
            return
        
        grid[i][j] = 'x'
        self._numIslandsHelper(i-1,j,grid)
        self._numIslandsHelper(i+1,j,grid)
        self._numIslandsHelper(i,j-1,grid)
        self._numIslandsHelper(i,j+1,grid)