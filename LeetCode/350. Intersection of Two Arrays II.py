# 还是不熟悉啊，调了半天写的这么臃肿，132ms...先放这吧

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans = []
        if len(nums1)>len(nums2):
            numsmax = nums1
            numsmin = nums2
        else:
            numsmax = nums2
            numsmin = nums1
        for x in numsmin:
            if x in numsmax and x not in ans:
                if numsmax.count(x)>numsmin.count(x):
                    numc = numsmin.count(x)
                else:
                    numc = numsmax.count(x)
                for i in range(0,numc):
                    ans.append(x)
        return ans
