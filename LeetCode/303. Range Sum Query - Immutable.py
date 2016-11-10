# 用一个数组记录累积和，这样会快些，因为要调用很多次。还有加深熟悉函数的init啊...

class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        if len(nums)==0:
            return None
        sumN = [nums[0]]
        for i in range(1,len(nums)):
            sumN.append(sumN[i-1]+nums[i])
        self.sumN = sumN
    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        if i==0:
            return self.sumN[j]
        else:
            return self.sumN[j]-self.sumN[i-1]


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)
