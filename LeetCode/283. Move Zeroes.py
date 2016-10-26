# 过是过了，但是时间只超过很小部分人。肯定不满足第二点的要求——很少的操作。因为j每一次都会从最后一个开始比较，应该考虑每次记录下最后一个确定为0的位置。
# 或者用类似快排的思想。

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        for i in range(0,l):
            if nums[i]==0:
                for j in range(l,0,-1):
                    if i<j and nums[j-1]!=0:
                        x = nums[j-1]
                        nums[j-1] = nums[i]
                        nums[i] = x
                        
# 改进版
