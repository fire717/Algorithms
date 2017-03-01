# 不知道满不满足O(k) extra space

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        ans = [[] for i in range(rowIndex+1)]                
        for i in xrange(rowIndex+1):
            for j in xrange(i+1):
                if j==0 or j==i:
                    ans[i].append(1)
                else:
                    ans[i].append(ans[i-1][j-1]+ans[i-1][j])
        return ans[-1]
