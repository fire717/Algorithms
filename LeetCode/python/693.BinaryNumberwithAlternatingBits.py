#暴力法 35ms-50%
class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        x = str(bin(n))
        for i in range(len(x)-1):
            if x[i] == x[i+1]:
                return False
        return True
      
