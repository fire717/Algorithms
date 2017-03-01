# 一开始想复杂了。


class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        last = []
        for x in nums1:
            if x in nums2 and x not in last:        #这里注意，不能省略第二个x
                    last.append(x)
        return last
