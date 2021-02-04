#952 ms  - 53.51%
class Solution:
    def findMaxAverage(self, nums, k: int) -> float:
        n = len(nums)
        max_sum = sum(nums[:k])
        last_sum = max_sum
        for left in range(1,n):
            if(left+k-1>=n):
                break
            this_sum = last_sum+nums[left+k-1]-(nums[left-1])
            if this_sum>max_sum:
                max_sum = this_sum
            last_sum = this_sum
        return max_sum / k
