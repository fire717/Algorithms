class Solution(object):
    def rob(self, nums):
        def _rob(nums):
            a, b = 0, 0
            for i in xrange(len(nums)):
                a, b = b, max(a + nums[i], b)#a记录上一次b的值，b这次的值为a(即上次的b)加上当前值和不加的最大值
            return b
        a, b = _rob(nums[:-1]), _rob(nums[1:])#分别计算不要尾节点和头结点的，因为两者只能选一个
        return max(a, b) if len(nums) is not 1 else nums[0] #len=0,1时都可以返回nums[0]
