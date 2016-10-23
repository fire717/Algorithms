#  一开始的版本，应该是 一般思路，结果 提示超时
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = len(s)
        ans = ''
        for i in range(0,l):
            ans=ans+s[l-1-i]
        return ans
        
# 无奈查了下，原来python字符串能直接转换。。。基础不扎实啊T.T
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]
