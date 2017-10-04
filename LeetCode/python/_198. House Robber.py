# 开始想简单了，觉得从最大的开始依次来就行，还调整了半天索引号的问题，结果提交遇到[2，3，3]的情况就错了。原来想简单了...
# 难道又是动态规划么...

# 最开始的版本
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        while len(nums)>0:
            t = 0
            indext = 0
            for i in range(0,len(nums)):
                if nums[i]>t:
                    t=nums[i]
                    indext = i
                    print indext
            ans+=t
            del nums[indext]
            if indext+1<=len(nums):
                del nums[indext]
            print nums
            if indext == 1:
                del nums[0]
        return ans
        
# 查了下，的确是动态规划，但是说j题目的意思居然是固定从第一个开始吗？我又想复杂了，以为任意开始...
# 今天就做这一道，不过熟悉动态规划！DP
#如果输入是v1v2...vm，用S[i]表示从v1v2...vi能偷到的最大价值。
#递归子问题：S[i] = max(S[i-1], vi + S[i-2])
#初如条件：S[0] = 0 S[1] = v1 S[2] = max(S[1], v2 + S[0])
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        elif n == 1:
            return nums[0]
        else:
            s = [0 for i in range(n)]              //快学习这种写法！
            s[0] = nums[0]
            s[1] = max(nums[0], nums[1])
            for i in range(2,n):
                s[i] = max(s[i-1], s[i-2] + nums[i])
            return s[n-1]
