# 这道题要一次性作对不容易，主要还是在回文数的理解上，要考虑各种边界情况，这应该是目前为止调试次数最多的一道题吧...

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        lens = 0
        oddn = []
        hasodd  = 0
        for x in s:
            if s.count(x)%2!=0:
                hasodd = 1
                if x not in oddn:
                    oddn+=x
            lens+=1
        return lens-len(oddn)+hasodd
