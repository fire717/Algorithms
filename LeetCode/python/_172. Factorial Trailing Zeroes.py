# 还是看不懂题目，大概试了下，明白了，求N阶后末尾0的个数
# 随便写了个，果然超时了，这应该是n的复杂度
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        t = 1
        ans = 0
        for i in xrange(1,n+1):
            t*=i
        for x in str(t)[::-1]:
            if x=='0':
                ans+=1
            else:
                break
        return ans
        
#要求对数复杂度，但是求阶就是n的复杂度了...
#解题思路
#通过因数分解知道，10是由2和5相乘得到的，而在n的阶乘中，因子2的数目总是比5多的，所以最终末尾有几个零取决于其中有几个5。
#1到n中能够整除5的数中有一个5，能整除25的数有2个5（且其中一个在整除5中已经计算过）…
#所以只要将n不断除以5后的结果相加，就可以得到因子中所有5的数目，也就得到了最终末尾零的数目。
#Python2.2以及以后的版本中增加了一个算术运算符" // "来表示整数除法，返回不大于结果的一个最大的整数
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0        
        while n:            
            n //= 5            
            count += n        
        return count
