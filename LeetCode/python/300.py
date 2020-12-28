"""
自己做出来的动态规划题，但实际耗时还有空间啊

执行用时：
2380 ms
, 在所有 Python3 提交中击败了
27.72%
的用户
内存消耗：
14.8 MB
, 在所有 Python3 提交中击败了
16.33%
的用户

"""

class Solution:
    def lengthOfLIS(self, nums):
        len_nums = len(nums)
        #状态： z[i][j] 表示 以元素j结尾的长度为i的数组的最大递增子序列长度
        #转移方程： z[i][j] = max( max(z[i-1][j-1]+1 where nums[i]>z[i][j-1]), 
        #                                    z[i-1][j]+1 where nums[i]>z[i][j-1])
        #限制：i固定时长度也固定
        z = [[1]*len_nums]*len_nums

        for i in range(1,len_nums):
            length_tmp = 1
            for j in range(0,i):
                if nums[i]>nums[j]:
                    value = z[i-1][j]+1
                    if value>length_tmp:
                        length_tmp = value

            if length_tmp>1:
                z[i][j+1] = length_tmp


        return max(z[len_nums-1]) 
