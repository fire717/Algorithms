class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        for i in range(1,len(A)):
            if A[i]>A[i-1]:
                continue
            else:
                return i-1
