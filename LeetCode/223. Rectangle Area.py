# 一开始没弄清题意，原来是求总面积，不是交面积...关键是判断是否有交集
class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        areaA=(C-A)*(D-B)
        areaB=(G-E)*(H-F)
        if E>C or A>G or B>H or F>D:
            samearea = 0
        else:
            samearea = (min(C,G)-max(A,E))*(min(D,H)-max(B,F))
        return areaA+areaB-samearea
