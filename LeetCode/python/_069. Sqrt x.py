#觉得简单，然后memory error了
#把range换成xrange就好了（range是一次性生成一个list，xrange是生成器）
#但是又超时了..1745536076的时候
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        sx = str(x)
        l=len(sx)
        tmp=0
        for i in xrange(int(10**int(l/2-1)),x+3):
            t = i*i
            if t == x:
                return i
            elif t>x:
                return i-1
#也想起之前看麻省理工的时候学的那个求平方根的方法，使用递归
#但是发现maximum recursion depth exceeded...
#好吧，又查了
#发现跟mit那个原理类似，但是不用递归
#好像是叫Newton method，收敛更快
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        r = x  #从大到小，遇到第一个小于等于的就输出，比我判断等于大于好
        while r*r > x:
            r = (r + x/r) / 2
        return r
