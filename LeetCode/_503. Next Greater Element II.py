#自己写了初版，能通过测试，但是提交时超时了
class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l=len(nums)
        res=[]
        for i in range(l):
            tmp=0
            for j in range(i+1,l):
                if nums[j]>nums[i]:
                    res.append(nums[j])
                    tmp=1
                    break
            if tmp==0 and i>=1:
                for j in range(0,i):
                    if nums[j]>nums[i]:
                        res.append(nums[j])
                        tmp=1
                        break
            if tmp==0:
                res.append(-1)
        return res
 
 #查的AC版本
 #通过使用栈，时间复杂度由O(n^2)下降到O(n)
 #对于循环数组的处理，将nums数组遍历两次，下标对len(nums)取模
 class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        stack = []
        size = len(nums)
        ans = [-1] * size
        for x in range(size * 2):
            i = x % size
            while stack and nums[stack[-1]] < nums[i]:
                ans[stack.pop()] = nums[i]
            stack.append(i)
        return ans
