#64ms - 86%  一次AC
class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count = 0
        h = len(grid)
        w = len(grid[0])
        max_row = [0] * w
        max_col = [0] * h
        #遍历一次获取行列各最大值
        for i in range(h):
            for j in range(w):
                if grid[i][j]>max_row[j]:
                    max_row[j] = grid[i][j]
                if grid[i][j]>max_col[i]:
                    max_col[i] = grid[i][j]
        for i in range(h):
            for j in range(w):   
                top = min(max_col[i],max_row[j])
                if grid[i][j]<top:
                    count = count+top-grid[i][j]
        return count
