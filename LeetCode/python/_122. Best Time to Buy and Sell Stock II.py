#Basically, if tomorrow's price is higher than today's, we buy it today and sell tomorrow. Otherwise, we don't. 
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        return sum(max(prices[i + 1] - prices[i], 0) for i in range(len(prices) - 1))
