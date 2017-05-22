#92ms-70%
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        tmp = 0
        for i in xrange(len(nums)):
            if nums[i]==1:
                tmp+=1
            else:
                res = max(res,tmp)
                tmp = 0
    res = max(res,tmp) #防止只有1
        return res
