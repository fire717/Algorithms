#不知道这道题为什么这么出...可能是要优化吧
#我才65 ms-17%，不知道优化的思路,是要自己重写吗，那有点麻烦，要分成正负，大小于1的情况
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        return x**n
