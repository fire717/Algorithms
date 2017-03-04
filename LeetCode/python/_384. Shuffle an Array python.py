#以后即使自己查的也要看懂写好注释了，这样才有收获
#好吧，查的这个想法跟自己差不多，还是用到了random
import random
class Solution(object):

    def __init__(self, nums):
        self.nums = nums

    def reset(self):
        return self.nums

    def shuffle(self):
        ans = self.nums[:]                     # copy list
        for i in range(len(ans)-1, 0, -1):     # start from end
            j = random.randrange(0, i+1)    # generate random index   从大范围到小/randrange返回指定递增基数集合中的一个随机数，基数缺省值为1
            ans[i], ans[j] = ans[j], ans[i]    # swap  python这样交换很方便啊，不用中间变量
        return ans



# Python hack....
#对于单行函数，使用lambda可以省去定义函数的过程，让代码更加精简。在非多次调用的函数的情况下，lambda表达式即用既得，提高性能
class Solution(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.reset = lambda: nums
        self.shuffle = lambda: random.sample(nums, len(nums))

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
