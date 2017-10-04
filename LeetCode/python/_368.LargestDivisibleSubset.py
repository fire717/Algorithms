class Solution(object):
    def largestDivisibleSubset(self, nums):
        S = {-1: set()}
        for x in sorted(nums): #直接写sorted(nums)
            S[x] = max((S[d] for d in S if x % d == 0), key=len) | {x}
            #max也可以传入key参数
        return list(max(S.values(), key=len))#取字典S的值的MAX，判定指标是长度
