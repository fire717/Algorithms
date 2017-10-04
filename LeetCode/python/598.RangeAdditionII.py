#处理下两种特殊情况就好了
#42ms-91%
class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        if not ops:
            return m*n
        if m<1 or n<1:
            return 0
        minM = 40000
        minN = 40000
        for li in ops:
            if li[0] < minM:
                minM = li[0]
            if li[1] < minN:
                minN = li[1]
        return minM*minN
