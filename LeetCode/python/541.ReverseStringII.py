#62ms-21%
class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        t=0
        while t<len(s):
           s=s.replace(s[t:t+k],s[t:t+k][::-1],1) #字符串逆序：s[::-1] / replace后要赋值
           t+=2*k
        return s
