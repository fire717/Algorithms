#发现更新了一些easy的题，这道不就是完数嘛
#然而。提交时超时了
class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num<=0:
            return False
        divn = [1]
        for i in xrange(2,num/2+3):
            if num%i == 0:
                divn.append(i)
            print divn
        if num == sum(divn):
            return True
        else:return False
        
        
  #One thing to keep in mind is the stopping condition of for loop is less or equal to SQRT.
  class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0: return False
        ans, SQRT = 0, int(num ** 0.5)
        ans = sum(i + num//i for i in range(1, SQRT+1) if not num % i)
        if num == SQRT ** 2: ans -= SQRT
        return ans - num == num
