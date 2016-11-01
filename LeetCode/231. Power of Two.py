class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n==0:return False
        if n%2 == 0 or n==1:
            if n/2==1 or n==1:
                return True
            n/=2
            return self.isPowerOfTwo(n)   #还是要加return才行
        else:return False
