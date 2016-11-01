# 第一反应，双重循环，果然超时了...
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxP = 0
        for buy in range(0,len(prices)-1):
            for sell in range(buy+1,len(prices)):
                if prices[sell]-prices[buy]>maxP:
                    maxP = prices[sell]-prices[buy]
        return maxP
        
# 【动态规划法】。从前向后遍历数组，记录当前出现过的最低价格，作为买入价格，并计算以当天价格出售的收益，作为可能的最大收益。
# 整个遍历过程中，出现过的最大收益就是所求。

class Solution(object):
    def maxProfit(self, prices):
        if len(prices)<2:
            return  0
        maxpf=0
        low=prices[0]
        for i in range(len(prices)):
            if prices[i]<low:
                low=prices[i]                         #原来就是设置一个最小的锚点
            maxpf=max(prices[i]-low,maxpf)            #max用法要记住，比if else简洁多了
        return maxpf
