#112ms - 61.68%
class Solution:
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = len(nums)
        tmp = [0] * l
        for i in range(l):
            if tmp[nums[i]-1] == 0:
                tmp[nums[i]-1] = 1
            else:
                dup = nums[i]
        return [dup, tmp.index(0)+1]
