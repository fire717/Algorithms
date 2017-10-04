# 这道题还算简单 只是时间76ms-32%
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        nums.sort()
        for i in xrange(l):
            if i != nums[i]:
                return i
        return l
