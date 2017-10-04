# 一看题目很简单，瞬间写好一个，测试通过，然后提交，超时了...
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        t = []
        ans=[]
        for x in nums:
            if x not in t:
                t.append(x)
            else:
                ans.append(x)
        return ans
#虽然for循环一遍，但是应该是每次用in来判断比较费时吧         
#论坛看的版本，using the input array itself as a hash to store which numbers have been seen before
#之前也想到用空列表，数字来索引，后来超出范围了，没注意题目1 ≤ a[i] ≤ n
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for x in nums:
            if nums[abs(x)-1] < 0:
                res.append(abs(x))
            else:
                nums[abs(x)-1] *= -1
        return res
