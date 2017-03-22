# 想到两种方法

#1.记录每种颜色的次数，然后每次通过x[i:i]来插入
#2.遍历一遍，记录数量，直接输出
#结果尝试第一种的时候提示，不要返回任何值...也就是改变原序列
#对了，限制不能用自带的sort(虽然试了下可以AC...)

#然后想到交换排序，但是不知道为什么对[1,0]测试的时候老是超时。

#好吧要continue跳出继续

#修修补补弄了好久啊...
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        #交换排序吧
        l = len(nums)
        i = 0
        while i < l-1 :
            if nums[i] == 0:
                j = 1
                k = 1
                while j <= l-i-1:
                    if nums[i+j] == 0:
                        j += 1
                        k += 1
                        continue
                    j += 1
                i+=k
                continue
            elif nums[i] == 1:
                j = 1
                while j <= l-i-1:
                    if nums[i+j] == 0:
                        nums[i],nums[i+j] = 0,1
                        break
                    else:
                        j += 1
                        continue
                    break
                i+=1
                continue
            else:
                j = 1
                while j <= l-1:
                    if nums[-j] != 2:
                        nums[i],nums[-j] = nums[-j],nums[i]
                        l-=j
                        print nums
                        break
                    else:
                        j+=1
                
                i+=1
                continue
                
  
  
  #放弃了..估计改是解决不了的...
  
  #好像是Lomuto partition algorithm什么快排
  class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = j = 0
        for k in xrange(len(nums)):
            v = nums[k]
            nums[k] = 2
            if v < 2:
                nums[j] = 1
                j += 1
            if v == 0:
                nums[i] = 0
                i += 1
                
                
 #自己突然又有了灵感，用最上面的第二种方法，也过来，46ms-46%
 
 class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        r = 0
        w = 0
        b = 0
        for i,n in enumerate(nums):
            if n == 0:r+=1
            if n == 1:w+=1
            if n == 2:b+=1
        for i in xrange(len(nums)):
            if i < r:
                nums[i] = 0
            if i >= r and i < r+w:
                nums[i] = 1
            if i >= r+w:
                nums[i] = 2
                        
