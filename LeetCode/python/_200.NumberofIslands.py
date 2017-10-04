#这种题没啥头绪...
class Solution(object):
    def numIslands(self, grid):
        def sink(i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] == '1': #如果在长度范围内且等于1
                grid[i][j] = '0'  #置0
                map(sink, (i+1, i-1, i, i), (j, j, j+1, j-1)) #对上下左右的元素迭代
                return 1 #返回一个1
            return 0 #=0则返回0
        return sum(sink(i, j) for i in range(len(grid)) for j in range(len(grid[i]))) #整体遍历一遍求和
