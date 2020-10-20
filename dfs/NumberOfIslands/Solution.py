class Solution:
    def numIslands(self, grid):
        def sinkIsland(grid, r, c):
            if grid[r][c] == '1':
                grid[r][c] = '0'
            else:
                return
            
            if r + 1 < len(grid):
                sinkIsland(grid, r+1, c)
            if r - 1 >= 0:
                sinkIsland(grid, r-1, c)
            if c + 1 < len(grid[0]):
                sinkIsland(grid, r, c+1)
            if c-1 >= 0:
                sinkIsland(grid, r, c-1)
                
        counter = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    counter += 1
                    sinkIsland(grid,r,c)
                    
        return counter
    
test = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]

print(Solution().numIslands(test))