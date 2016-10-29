# 第一个版本在那个全是1和2的测试中显示超出最大时间了...然后加了一个判断的代码，55ms pass并且超过95%的人...

# 1st ver /主要是每一次都会进行if判断，if中还有count
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        countN = 0
        num = 0
        for i in range(0,len(nums)/2+1):
            if nums.count(nums[i])>countN:
                countN = nums.count(nums[i])
                num = nums[i]
        return num



# Pass ver  加入了一个检测重复的队列，这样每次if只需要判断是否在nn中，大多数在的情况下直接pass几乎不花时间
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        countN = 0
        num = 0
        nn = []
        for i in range(0,len(nums)/2+1):
            if nums[i] not in nn:
                nn.append(nums[i])
                if nums.count(nums[i])>countN:
                    countN = nums.count(nums[i])
                    num = nums[i]
        return num
