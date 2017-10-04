
#这道题比较典型吧，要求不知道长度的组合数，即使想暴力法也不知道for循环的次数。除非全部写出来再用if判断...
#没思路...
#论坛查了下，这个很不错，时间也快。思路完全就不是暴力的那种，而是利用递归，学习学习
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k==1:
            return [[i] for i in range(1,n+1)]
        elif k==n:  #先考虑两种特殊情况
            return [[i for i in range(1,n+1)]]
        else:
            rs=[]
            rs+=self.combine(n-1,k) #递归时分两种，一种是不要第n个元素，一种是全部要第n个元素，这行是第一种
            part=self.combine(n-1,k-1) #这行先把不要第n个元素的k-1的组合写出来
            for ls in part:   #再全部加上第n个元素
                ls.append(n)
            rs+=part   #两部分相加就是总的
            return rs
