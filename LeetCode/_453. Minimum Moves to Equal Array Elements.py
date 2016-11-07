# 自己想了好久写了一个，居然提交[1,2147483647]超时了....唉 感觉思想挺好的啊，记录下吧
class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        maxn = max(nums)
        minn = min(nums)
        count = 0
        while maxn!=minn:              
            ifmax = 1                              # z通过这个值来判断是否最大值有多个相同的，这样只加一次
            passmax = 0                           #防止误判，设置一个值检测是否经过了最大值
            for j in range(0,l):                    #给除了最大值其他每个元素加一
                if nums[j]==maxn:
                    maxn+=1
                    passmax = 1
                    continue
                if nums[j] == maxn-1 and passmax:
                    nums[j]+=1
                    ifmax = 0
                else:
                    nums[j]+=1
                    
            if ifmax:
                maxn-=1
            minn+=1
            count+=1
            
        return count
        
# 
