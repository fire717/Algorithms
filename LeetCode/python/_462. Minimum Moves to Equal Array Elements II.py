# 感觉不难，求平均值然后求差值和
#但是不知道为什么提交时就遇到一个问题了[1,0,0,8,6]我是16要求14，我口算一遍也是16啊。可能是题目理解不到位吧
#初版：
class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = 0
        l = 0
        for x in nums:
            total+=x
            l+=1
        ave = total/l
        ans = 0
        for x in nums:
            ans+=abs(ave-x)
        return ans
# 查了下，果然不是平均数，要用中位数，口算了一下，果然中位数1的话就是14了！恩，这样可以让一个数字一步不动
# 假设平均值大1，那么小的两个数多加2，大的多减2抵消了，中位数白白加1，所以要用中位数！
# 把平均数改为中位数就可以AC了，只是相当于遍历了72%，代码也不够简洁。
class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = 0
        l = 0
        for x in nums:
            total+=x
            l+=1
        nums.sort()
        mid = nums[l/2]
        ans = 0
        for x in nums:
            ans+=abs(mid-x)
        return ans
