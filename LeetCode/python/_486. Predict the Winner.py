#利用dp..只能写到这一步了...
#16行有问题，因为这个并不是一直让你选的。A选了后，B选，B同样会最大化收益的去选择
#突然又有想法了，改了下，分别为求min和max，然后交替迭代即可   
#但是还是没过[0,0,7,6,5,6,1]，不知道怎么错了...
class Solution(object):
    def minA(self,nums1):
        if len(nums1)==3:
            n0 = nums1[:]
            n0.sort()
            return n0[2]+min(nums1[0],nums1[2])
        if len(nums1)==4:
            n1 = nums1[1:]
            n1.sort()
            n2 = nums1[:-1]
            n2.sort()
            left2min = n1[1]
            right2min =n2[1] 
            return min((nums1[0]+left2min),(nums1[0]+nums1[2]),(nums1[-1]+right2min),(nums1[-1]+nums1[1]))
        minASum = min((nums1[0]+self.maxA(nums1[1:])),(nums1[-1]+self.maxA(nums1[:-1])))  
        return minASum
    def maxA(self,nums2):
        if len(nums2)==3:
            n0 = nums2[:]
            n0.sort()
            return n0[0]+max(nums2[0],nums2[2])
        if len(nums2)==4:
            n1 = nums2[1:]
            n1.sort()
            n2 = nums2[:-1]
            n2.sort()
            left2max = n1[1]
            right2max =n2[1] 
            return max((nums2[0]+left2max),(nums2[0]+nums2[2]),(nums2[-1]+right2max),(nums2[-1]+nums2[1]))
        maxASum = max((nums2[0]+self.minA(nums2[1:])),(nums2[-1]+self.minA(nums2[:-1])))  
        return maxASum
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #思路：利用DP，先求出A能得出的最大的值，再比较B的值从而判断。
        if len(nums)<3:
            return True
        sumA = self.maxA(nums)
        if sumA >sum(nums)-sumA:
            return True
        else:
            return False
            
 #AC版本
 class Solution(object):
    def PredictTheWinner(self, nums):
        def check(left, right, memo): #用两端索引来迭代，便于存入memo并比较
            if left > right:
                return 0
            if left == right: #左右索引相等时停止
                return nums[left]
            if not (left, right) in memo:
                ss = sum(nums[left: right + 1])
                l, r = ss - check(left + 1, right, memo) + nums[left], ss - check(left, right - 1, memo) + nums[right]
                #因为两人交替选，所以这里迭代时用总和减去选择某端的最大值（相当于对方选的）
                memo[(left, right)] = max(l, r) #保存一堆索引号能取得的最大值
            return memo[(left, right)]

        s = sum(nums)
        c1 = check(0, len(nums) - 1, {})
        return c1 >= s - c1#不用写if直接写式子就可以返回布尔值了
        
