# 主要是要in-place比较麻烦。查的思路先把前n-k个数字翻转一下，再把后k个数字翻转一下，最后再把整个数组翻转一下 
# 熟悉列表的reverse()方法，直接反转

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        if n<2 or k==0:
            return 
        k=k%n
        n1=nums[:n-k]
        n1.reverse()
        n2=nums[n-k:]
        n2.reverse()
        nums[:]=list(n1+n2)
        nums.reverse()         
