# 26ms超过99.77%...我还以为要用到什么高深的算法比如动态规划呢，结果就2除就可以了吗

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = 0
        b = n/2
        c = n
        while True:
            if isBadVersion(b):
                if b == 1:
                    return b
                c = b
                b = (b+a)/2
            else:
                if isBadVersion(b+1):
                    return b+1
                a = b
                b = (b+c)/2
