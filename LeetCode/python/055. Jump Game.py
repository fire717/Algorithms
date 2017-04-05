#又是调整边界条件弄了一会，不过还好没多久弄出来了

#52 ms-87%

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums[0] == 0 and nums[-1] != 0:
            return False
        for i in xrange(len(nums)-1):
            if nums[i] == 1:
                continue
            if nums[i] == 0:
                b=0
                for j in xrange(1,i+1): #为0时往前遍历找到一个值大于步数差的，有则跳出继续，无且遍历完了则return
                    if nums[i-j]>j:
                        b = 1
                        break
                if b==0:
                    return False
        return True
