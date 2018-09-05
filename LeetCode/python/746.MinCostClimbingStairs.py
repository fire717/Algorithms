# 64 ms - 74.36%
class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        l = len(cost)
        if l==0 or l==1:
            return 0
        elif l==2:
            return min(cost[0],cost[1])
        else:
            history = cost[:2]+[0]*(l-2)
            this = 2
            while this<l-1:
                history[this] = min(history[this-2]+cost[this],history[this-1]+cost[this])
                this+=1
                #print(history)
            history[this] = min(history[this-2]+cost[this],history[this-1])#边界情况 最后一步可以不踩
            return history[-1]
