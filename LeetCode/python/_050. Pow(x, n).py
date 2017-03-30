#不知道这道题为什么这么出...可能是要优化吧
#我才65 ms-17%，不知道优化的思路,是要自己重写吗，那有点麻烦，要分成正负的情况
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        return x**n
    
#写成这样超时了。。
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        ans=1.0
        if n>=0:
            for i in xrange(n):
                ans*=x
        else:
            for i in xrange(-n):
                ans*=x
            ans=1/ans    
        return ans
    
  #还是查查吧 递归
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0: 
            return 1
        if n == -1: 
            return 1 / x
        return self.myPow(x * x, n / 2) * ([1, x][n % 2])
