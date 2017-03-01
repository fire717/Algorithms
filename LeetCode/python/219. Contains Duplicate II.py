# 最后还是调出来了。62 ms-43%。不过调了好久啊..各种边界条件，还是题目没理解透彻

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        '''
        ddd
        '''
        t = {}
        l = sl = len(nums)
        if l < 2 :
            return False
        if k==l and nums[0]==nums[-1]:
            return True
        for i in xrange(l):
            if nums[i] in t and i-t[nums[i]]<=k:
                return True
            else:
                t[nums[i]]=i
        return False
