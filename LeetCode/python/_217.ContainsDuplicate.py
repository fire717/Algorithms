# 自己写了几个都超时了，然后一查就一行搞定...完全忘了set集合的概念...学习

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) != len(set(nums))
