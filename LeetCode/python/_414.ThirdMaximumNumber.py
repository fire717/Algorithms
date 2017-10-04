# 用 List[-1]算不算作弊呢...肯定是非主流方法，因为时间只打败1%....先放这吧，至少是自己想很久弄出来的.

class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        t = []
        for i in nums:
            if i not in t:
                t.append(i)
        t.sort()
        if len(t)<3:
            return t[-1]
        if t[-1] == t[-2] or t[-2] == t[-3]:
            return t[-1]
        else:
            return t[-3]
