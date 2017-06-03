#太简单了吧，。。一次性AC
#不过52 ms-24%...
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = len(nums)
        for i in xrange(l):
            if nums[i]>=target:
                return i
        return l
