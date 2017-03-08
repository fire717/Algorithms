#list求和是sum(list)而不是list.sum()...自己搞混了好久
#说是和矩阵链乘很相似，是典型的动态规划问
#问题转换为能不能找到一个非空子集合，使得其数字之和为target
'''
把list分成两个，一个为+的，一个为-的，则有
sum(P) - sum(N) = target
sum(P) + sum(N) + sum(P) - sum(N) = sum(P) + sum(N) + target 
                       2 * sum(P) = sum(nums) + target
'''

class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        if not nums: #nums为空时相当于false，加not则为true，非空时not num为false
            return 0
        dic = {nums[0]: 1, -nums[0]: 1} if nums[0] != 0 else {0: 2}
        
        for i in range(1, len(nums)):
            tdic = {}
            for d in dic:
                tdic[d + nums[i]] = tdic.get(d + nums[i], 0) + dic.get(d, 0)
                tdic[d - nums[i]] = tdic.get(d - nums[i], 0) + dic.get(d, 0)
            dic = tdic
            
        return dic.get(S, 0)
