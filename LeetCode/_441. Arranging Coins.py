# 这就是个数学题，我自己写了个解法提交结果报错Memory Limit Exceeded
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        counti = 0
        for i in range(1,n/2+1):
            counti+=i
            if n-counti<i+1:
                return i
              
# 无奈搜索了一下：
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int

        数学推导
        (1+k)*k/2 = n
        k+k*k = 2*n
        k*k + k + 0.25 = 2*n + 0.25
        (k + 0.5) ^ 2 = 2*n +0.25
        k + 0.5 = sqrt(2*n + 0.25)
        k = sqrt(2*n + 0.25) - 0.5
        """
        return int(math.sqrt(2*n+0.25)-0.5)
