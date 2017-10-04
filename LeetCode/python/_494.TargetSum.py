#list求和是sum(list)而不是list.sum()...自己搞混了好久
#说是和矩阵链乘很相似，是典型的动态规划问
#问题转换为能不能找到一个非空子集合，使得其数字之和为（sum(nums) + target ）/ 2
'''
把list分成两个，一个为+的，一个为-的，则有
sum(P) - sum(N) = target
sum(P) + sum(N) + sum(P) - sum(N) = sum(P) + sum(N) + target 
                       2 * sum(P) = sum(nums) + target
'''

#在官方论坛看到的解法，大致懂了，即用字典保存从1开始的依次遍历的情况，每多一个数据，即等于到达上一个位置的数量分别+-
#但是好像没用到DP...
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
          #当元素为0时则个数+2，因为+-0都可以，元素不为0时则+n为一种计算，-n为另一种   / 可想像只有一个元素的情况
        
        for i in range(1, len(nums)): #从1开始，因为0在上面已经处理了
            tdic = {}     #空字典记录前面能取到某值的个数
            for d in dic:   #分别遍历已有的记录，计算到达当前位置的个数=当前位置已有记录数加上到达前面的位置的个数
                tdic[d + nums[i]] = tdic.get(d + nums[i], 0) + dic.get(d, 0)
                tdic[d - nums[i]] = tdic.get(d - nums[i], 0) + dic.get(d, 0)
            dic = tdic
            
        return dic.get(S, 0)
