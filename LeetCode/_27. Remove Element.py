# 调了半天搞得头昏脑涨，感觉题目就没弄清，明明说rtype为int，例子又是list..
# 查了还是没搞清楚..这题...唉...

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        index = 0  
        for num in nums:  
            if num != val:  
                nums[index] = num  
                index += 1  
        return index  
                      
