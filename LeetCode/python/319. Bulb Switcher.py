#按题意暴力解法，提交时到999999 MLE
class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = []
        for i in range(0,n):
            res.append(1)
        for j in range(1,n+1):
            for k in range(j-1,n,j):
                res[k]+=1
        n = 0
        for x in res:
            if x%2==0:
                n+=1

        return n
#因为是MLE，所以肯定不是先生成一个初始的list了，还是要找规律，之前想过，但是要判断质数的话也要循环
#ac版本
#对于给定的 n，之前有 floor(n) 个完全平方数，也就是最后有 floor(n) 个灯泡是on状态。
#答案很简单，但是为什么是完全平方数呢？
class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        t = int(n**0.5)
        return t
