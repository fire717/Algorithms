# 啦啦 182ms-99.65%，而且整个就花了几分钟，而且代码还简洁，就调试了一次，考虑了负数的情况。
# 唯一不知道的是满不满足没用额外空间...虽然并没有用其他变量...

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x>=0:
            return (x+int(str(x)[::-1]))/2==x
        else:
            return (x+int(str(-x)[::-1]))/2==x
