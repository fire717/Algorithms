# 这种题目就算出的很好的，意思明了，限制清楚，但是又不容易想出来。
# 不用除法+O(n)我就不知道咋整了.

#解题思路： 利用返回的列表从前往后算一遍，再从后往前算一次即可(每个位置其实都是它前面所有数的乘积再乘上它后面所有数的乘积)
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [1]

        for i in range(1,len(nums)):
            result.append(result[i-1] * nums[i-1])
        print result
        product = 1
        for i in range(len(nums)-1,-1,-1):   #从大数降序遍历到小数，第1个-1指到-1为止，及0为止。最后1个-1代表逆序的意思
            result[i] = product * result[i]
            product *= nums[i]
        print product
        return result

