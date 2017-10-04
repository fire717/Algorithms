class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        nums.sort()
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i - 1]:
                l = len(res)
            for j in range(len(res) - l, len(res)):#从前往后依次遍历依次添加，然后继续遍历到添加过的
                res.append(res[j] + [nums[i]])
        return res
        
'''
1
[[], [1]]
2
[[], [1], [2]]
[[], [1], [2], [1, 2]]
[[], [1], [2], [1, 2], [2, 2]]
[[], [1], [2], [1, 2], [2, 2], [1, 2, 2]]
'''
