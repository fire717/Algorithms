#唉，昨天朋友来了，git push 就断了一天...
#这道题一开始想简单了，以为1-n每个数字都包含了..
#There is only one duplicate number in the array, but it could be repeated more than once.
#然后又要求空间O(1)，时间O(n2)

#先按常规思路想了一个：估计是空间O(n)，提交时也超时了
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tmp=[]
        for x in nums:
            if x in tmp:
                return x
            else:
                tmp.append(x)
                
#然后换了个思路：利用set()集合
#先去除重复元素，再分别求和，然后相减除以长度之差
#这样时间应该是O(n+n+n+n)=O(n),空间是O(1+n)=O(n),但是AC了..55ms-67.87%
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lN = len(nums)
        numsSingle=set(nums)
        lS = len(numsSingle)
        countN = 0
        countS = 0
        for x in nums:
            countN += x
        for x in numsSingle:
            countS +=x
        return (countN - countS)/(lN-lS)
