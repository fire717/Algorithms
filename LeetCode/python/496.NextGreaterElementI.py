#59ms-76%
class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        if not findNums:
            return []
        nn = {nums[-1]:-1}
        ln = len(nums)
        for i in xrange(ln-1):
            flag = 0 
            for j in xrange(i+1,ln):
                if nums[j]>nums[i]:
                    nn[nums[i]] = nums[j]
                    flag = 1 
                    break
            if flag==0:
                nn[nums[i]] = -1
   
        res = []
        for x in findNums:
            res.append(nn[x])
        return res
