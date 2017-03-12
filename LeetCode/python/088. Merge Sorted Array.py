# 不return原地操作，想到这个:
# 简单两行搞定，不算作弊吧，但是提交时，对[0]0[1]1错了，我返回[0,1]，答案是[1]，又不懂了，我又没读懂题目？
# 额，好像和m,n有关？
# 好吧，查了下翻译也不清楚，然后拿别人的测试，原来m,n的意思是分别取多少位（即限制长度）。我这个直接全部都取了、
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        nums1.extend(nums2)
        nums1.sort()

#查的解法 思想一样
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        x=nums1[0:m]  
        print x
        y=nums2[0:n]  
        print y
        x.extend(y)  
        print x
        x.sort()
        print x
        nums1[0:m+n]=x  
        
        
#还有这个简介解法
def merge(self, A, m, B, n):  
        A[m:] = B[:n]  
        A.sort()  
