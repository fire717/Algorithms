class Solution:
    def findLengthOfLCIS(self, nums) -> int:
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return 1
            
        res = 0
        count = 1
        len_nums = len(nums)
        for i in range(1, len_nums):
            if nums[i]>nums[i-1]:
                count+=1
                if i == len_nums-1 and count>res:
                    res = count
            else:
                if count>res:
                    res = count

                count = 1

        return res
