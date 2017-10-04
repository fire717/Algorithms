class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        curSum = maxSum = nums[0]
        for num in nums[1:]:
            curSum = max(num, curSum + num) #比较加上之前的大还是单独后一个大
            maxSum = max(maxSum, curSum)    #记录最大的值

        return maxSum
