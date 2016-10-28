# 49ms，又一个超过90%以上的，开心。

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        for i in range(0,len(s)):
            ans += (ord(s[i])-64)*26**(len(s)-i-1)
        return ans
