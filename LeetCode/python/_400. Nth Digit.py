#将整数序列划分为下列区间0-9,10-99,100-999...100000000-99999999,然后分区求值

class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        for i in range(9):
            d = 9 * 10 ** i
            if n <= d * (i + 1): break
            n -= d * (i + 1)
        n -= 1
        return int(str(10**i + n / (i + 1))[n % (i + 1)])
            
