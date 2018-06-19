# 70% 84ms
class Solution:
    def isSD(self,num):
        tmp = str(num)
        if '0' in tmp:
            return False
        for t in tmp:
            if num % int(t) != 0:
                return False
        return True
        
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        res = []
        for n in range(left,right+1):
            if self.isSD(n):
                res.append(n)
        return res
