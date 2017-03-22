#45ms-54%
#算是偷懒吗...反正熟悉了获取值得索引号的方法list.index()
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return nums.index(max(nums))
