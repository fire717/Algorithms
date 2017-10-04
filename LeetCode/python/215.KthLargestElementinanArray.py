#这不是一道送分题吗...题目中也没说不让用sort呀.....
#好吧，再刷一道.
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        return nums[-k]
