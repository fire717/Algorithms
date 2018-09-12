# 大致思路：按行列遍历，遇到1，就把count+1，同时采用DFS（或BFS这里是DFS）把所有连接的1置0，继续遍历
#84ms  92%
# DFS
class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0
        row = len(grid)
        col = len(grid[0])          
        count = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    self.dfs(grid, row, col, i, j)     
                    count += 1 
        return count 

    def dfs(self, grid, row, col, x, y):
        if grid[x][y] == '0':
            return
        grid[x][y] = '0'
        if x != 0:
            self.dfs(grid, row, col, x - 1, y)
        if x != row - 1:
            self.dfs(grid, row, col, x + 1, y)
        if y != 0:
            self.dfs(grid, row, col, x, y - 1)
        if y != col - 1:
            self.dfs(grid, row, col, x, y + 1)
