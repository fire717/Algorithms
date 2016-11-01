# 和power2一样，但是进阶要求，不用循环和递归不知道该怎么做...

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n==0:return False
        if n%3 == 0 or n==1:
            if n/3==1 or n==1:
                return True
            n/=3
            return self.isPowerOfThree(n)  
        else:return False
        
# 百度的进阶解法，先记录下,居然用了第三方库...不要脸！那也简单啊，或许还有其他办法吧...
# 求对数，然后乘方，判断得数是否相等

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and 3 ** round(math.log(n,3)) == n
