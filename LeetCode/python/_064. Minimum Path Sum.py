#典型的dp
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        now_min = {}
        l = len(grid)-1
        r = len(grid[0])-1
        now_min[(-1,-1)] = grid[-1][-1]
        for i in xrange(2,l+2):
            now_min[(-i,-1)] = grid[-i][-1]+now_min[(-i+1,-1)] 
        for j in xrange(2,r+2):
            now_min[(-1,-j)] = grid[-1][-j]+now_min[(-1,-j+1)] 
        for i in xrange(2,l+2):
            for j in xrange(2,r+2):
                now_min[(-i,-j)] = grid[-i][-j] + min(now_min.get((-i+1,-j),0),now_min.get((-i,-j+1),0))
        return now_min[(-l-1,-r-1)]
        
        
#但是超时了？
#查吧
#跟我的思路感觉差不多，但是没用到字典，直接grid保存？
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        for i in range(1, n):
            grid[0][i] += grid[0][i-1]
        for i in range(1, m):
            grid[i][0] += grid[i-1][0]
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[-1][-1]
