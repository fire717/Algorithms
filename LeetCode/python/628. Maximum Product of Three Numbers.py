#原来还有负数.
#162ms-13%  多算了两个...考虑到不可能三个都是负的，要么两个负，要么三个正
#删去后109-76%
class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return max(nums[0]*nums[1]*nums[-1],
                   nums[-1]*nums[-2]*nums[-3])
                   
