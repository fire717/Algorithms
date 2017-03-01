# 开始写了一个按上下界除以二的m，到1000居然超时了...

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# -1 : My number is lower    1 : My number is higher
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        board = 1
        while guess(n)!=0:
            if guess((n+board)/2)>0:
                n=(n+(n+board)/2)/2
                board=(n+board)/2
            elif guess((n+board)/2)<0:
                board = n/4
                n = (n+board)/2
            else:
                return (n+board)/2
        return n
        
        
# 统一设置到变量middle果然可读性高多了..而且其实方法是可行的，就是中间逻辑没理清楚...导致上下限乱变...
# 没查自己b手写了一下上下限变动然后改的，29ms超过98%~

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        board = 1
        while guess(n)!=0:
            middle = (n+board)/2
            if guess(middle)>0:
                board= middle
            elif guess(middle)<0:
                n = middle
            else:
                return middle
        return n
