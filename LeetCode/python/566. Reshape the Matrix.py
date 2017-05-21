#题不难，但是行列的问题输出调了很久
#开始是计算当前要输出的index。。。后来直接改成t然后每次加1了。。。
#169 ms-49%
class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        numr = len(nums)
        numc = len(nums[0])
        if numr*numc != r*c:
            return nums
        
        tmp = []
        for i in xrange(numr):
            for j in xrange(numc):
                tmp.append(nums[i][j])
        res = []
        t = 0
        for i in xrange(r):
            res.append([])
            for j in xrange(c):
                res[i].append(tmp[t])
                t += 1
        return res
