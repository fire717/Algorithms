#135 ms-67%
class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        ans = 0
        for i in range(0,len(nums),2):
            ans+=nums[i]
        return ans
