#难点在于 linear time and in O(1) 
#没思路，查了下，好像用Boyer-Moore Majority Vote algorithm
#这个算法是解决这样一个问题：从一个数组中找出出现半数以上的元素。 这道题是求n/3
'''
每次都找出一对不同的元素，从数组中删掉，直到数组为空或只有一种元素。 
不难证明，如果存在元素e出现频率超过半数，那么数组中最后剩下的就只有e。
'''

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums: 判断为空的写法
            return []
        count1, count2, candidate1, candidate2 = 0, 0, 0, 1 #设置两个初始值和计数
        for n in nums:
            if n == candidate1: 
                count1 += 1
            elif n == candidate2:
                count2 += 1
            elif count1 == 0: #若两个值为0时，重设为n
                candidate1, count1 = n, 1
            elif count2 == 0:
                candidate2, count2 = n, 1
            else: #若两个值都存在，但当前n都不等于其中两个，则两个计数都减1
                count1, count2 = count1 - 1, count2 - 1
                #事实当减为0时又重新为n初始值了
        return [n for n in (candidate1, candidate2)
                    if nums.count(n) > len(nums) // 3]
                    #为什么最后就一个(c1,c2)的元组了
                    #对了！因为要出现超过n/3次，不可能有三个数！
