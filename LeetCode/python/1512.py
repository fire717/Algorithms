
"""
执行用时：
36 ms
, 在所有 Python3 提交中击败了
88.73%
的用户
内存消耗：
14.9 MB
, 在所有 Python3 提交中击败了
5.24%
的用户
"""

class Solution:
    def numIdenticalPairs(self, nums ) -> int:
        res_dict = {}
        res = 0
        for i in range(len(nums)):
            if nums[i] in res_dict:
                res+=res_dict[nums[i]]
                res_dict[nums[i]]+=1
            else:
                res_dict[nums[i]]=1

        return res
