# python
# 这么简单第二次才AC，第一次是画蛇添足考虑效率问题先排序了一下，结果提交failed才意识到，排序后的索引值也变了。。。。T.T
# 还搞清楚了一点 range(a,b)的范围是包括a但不包括b

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return i,j
