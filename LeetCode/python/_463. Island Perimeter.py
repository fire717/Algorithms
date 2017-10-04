class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0

        def sum_adjacent(i, j):#返回1周围非1的和，每边非1对应周长加1
            adjacent = (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1),  #ad为一个set
            res = 0
            for x, y in adjacent:
                if x < 0 or y < 0 or x == len(grid) or y == len(grid[0]) or grid[x][y] == 0: #碰到边缘情况时加1
                    res += 1
            return res

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:   #遍历全部，等于1时，返回邻近岛屿的和
                    count += sum_adjacent(i, j)
        return count
