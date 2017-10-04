# 没遇到过如何判断无线循环为false，想到了异常处理，测试了一下可以，但是提交时还是超时了(测试a才42ms)...好吧，至少熟悉了try-except
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        count = 0
        loops =[]
        if n in loops
        while n>=1:
            count+=(n%10)**2
            n/=10
        return self.isHappy(count)
        
# “为了判断循环是否开始重复，要用一个字典（dict）或集合（set）来保存已经出现的数字，dict的效率更高。”
# 而且递归不能一直用一个字典，学习下while的写法
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        num_dict = {}

        while True:
            num_dict[n] = True
            sum = 0
            while(n>0):
                sum += (n%10)*(n%10)
                n /= 10
            if sum == 1:
                return True
            elif sum in num_dict:
                return False
            else:
                n = sum
