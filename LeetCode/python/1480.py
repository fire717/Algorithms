class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        return nums
        
        
""" 
提交了几次 波动性比较大

执行用时：
32 ms
, 在所有 Python3 提交中击败了
97.53%
的用户
内存消耗：
13.7 MB
, 在所有 Python3 提交中击败了
65.00%
的用户
"""
