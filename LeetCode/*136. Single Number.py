# 难点在于Your algorithm should have a linear runtime complexity.Could you implement it without using extra memory?
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = {}
        for i in nums:
            if i not in ans:
                ans[i] = 1
            else:
                ans[i] = 2
        for i in ans:
            if ans[i] == 1:
                last = i
                break
            
        return last
        
