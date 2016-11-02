# 又是一个数学问题，用递归写出来提示TLE..
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=0:
            return 0
        if n==1:
            return 1
        if n==2:
            return 2
        else:
            return  self.climbStairs(n-1)+self.climbStairs(n-2)

# 非递归
#   f(n)=f(n-1)+f(n-2)。自底向上。
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = []  
        a.append(1)  
        a.append(1)  
          
        for i in range(2, n + 1):  
            a.append(a[i - 1] + a[i - 2])  
          
        return a[n]  
