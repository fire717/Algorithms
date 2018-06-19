#60 ms
class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        tmp1 = [line[::-1] for line in A]
        tmp2 = [[1-x for x in line] for line in tmp1 ]
        return tmp2
