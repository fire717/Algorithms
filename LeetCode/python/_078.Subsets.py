#好吧，放弃了...调试了大半小时做成这样...
#能输出3个元素的，四个元素时就差一个子列表了...而且写的也丑也复杂
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans=[[]]
        l = len(nums)
        for i in nums:
            ans.append([i])
        lenAns = 1
        while lenAns < l : #从1开始到l-1，指当前要处理的长度
            newN = {} #新字典记录单个数的使用次数，避免重复
            for x in ans:  #遍历答案中已有的
                if x and len(x)==lenAns: #如果长度等于当前要处理的数组长度，
                    for i in range(0,len(nums)):  #再分别处理nums的单个数字加入进去
                        if nums[i] not in x and newN.get(nums[i],0)<i: #如果i不在x中，则先加入x的副本，生成一个当前长度+1的新数组，添加到ans中
                            #同时使用次数不能大于当前长度
                            t = x[:]  #必须这样复制，直接=号的话两者还是指向同一个list
                            t.append(nums[i])
                            ans.append(t)
                            if lenAns==l-1: #当长度为l-1时，加一次就可以返回了
                                return ans
                        newN[nums[i]] = newN.get(nums[i],0)+1 #每判断完一个数，就加一次使用次数
            lenAns+=1
        return ans
        

#AC
class Solution(object):
    def subsets(self, nums):
        nums.sort()
        result = [[]]
        for num in nums:
            result += [[num]+i for i in result] #好吧，list也可以用+
            #在第二次for时result也更新了
            #但是这样为什么不会有重复的呢？
            #推演了一遍懂了，外层循环保证每个数字只加一次，
            #同时前面又是排了序的..为什么？不需要啊...试了下，果然不需要排序...直接从36%到78%了..
        return result
