#自己直接写了个暴力解法，果然超时了... 
class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        ans = []
        j = 0
        l = len(A)
        if l==0:
            return 0
        while j<l:
            t = 0
            for i in xrange(l-j):
                t+=(i+j)*A[i]
            for k in xrange(j):
                t+=k*A[-j+k]
            ans.append(t)
            j+=1
        return max(ans)
        
# 假设数组A的长度为5，其旋转函数F的系数向量可表示出来
# 用每一行系数与其上一行做差，差值恰好为<code>sum(A) - size * A[size - x]，其中x为行数
# 因此，通过一次遍历即可求出F(0), F(1), ..., F(n-1)的最大值。
class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        size = len(A)
        sums = sum(A)
        sumn = sum(x * n for x, n in enumerate(A))
        ans = sumn
        for x in range(size - 1, 0, -1):
            sumn += sums - size * A[x]
            ans = max(ans, sumn)
        return ans
