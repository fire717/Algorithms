# 这个用了1800ms...打败0.1%的人..但是我简洁呀（自欺欺人..）

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        for i in range(0,len(s)):
            if s[i] not in s.replace(s[i],' ',1):
                return i
        return -1
