#本来写的递归，结果在1111111的时候超时了
#然后想用dp，但是一直写不好
#然后查了下，用的这个，应该是利用数学规律吧
class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        rtn = 0
        while n > 1:
            rtn += 1
            if n % 2 == 0:
                n /= 2        
            elif n % 4 == 1 or n == 3:  #这种情况就取-1
                n -= 1
            else:
                n += 1
        return rtn
        
        
        
#好吧，还是查了下利用字典的，好像不算是dp
#下次这种考虑下写成两个函数
class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = {1:0}
        return self.recRep(n, memo)
        
    def recRep(self, n, memo):
        if n in memo:
            return memo[n]
        if n % 2:
            memo[n] = 1 + min(self.recRep(n+1, memo), self.recRep(n-1, memo))
            return memo[n]
        else:
            memo[n] = 1 + self.recRep(n/2, memo)
            return memo[n]
