# 感觉有些 medium的题比easy简单...是因为语言的问题吗
# 想想如果用C的话就没有sort()和extend()了，可能要麻烦些，先放着吧，反正还要用C刷一遍
# 69ms-91%
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        x = []
        for l in matrix:
            x.extend(l)
        x.sort()
        return x[k-1]
