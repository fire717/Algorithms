# 原来列表也有加法！[a]+[b]=[a,b].思路L：利用位移运算

class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        ans = [0]
        for x in range(1, num + 1):
            ans += ans[x >> 1] + (x & 1),
        return ans
        

