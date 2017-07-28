#好久没刷了。。
#52ms-16%
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        i=0
        while i < num/2+2:
            i+=1
            if i*i==num:
                return True
            if i*i>num:
                return False
            
