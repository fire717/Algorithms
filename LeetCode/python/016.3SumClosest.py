#自己想了个然后调了很久，结果在250那超时了..
#记下思路吧，用2个list分别保存不同组合的和，然后再根据结果来选
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        count2 = []
        count3 = []
        for i in range(1,len(nums)):
            for x in count2:
                count3.append(x+nums[i])
            for x in nums[:i]:
                count2.append(x+nums[i])
        count3.sort()
        if count3[0]>=target:
            return count3[0]
        if count3[-1]<=target:
            return count3[-1]
        for i in range(0,len(count3)-1):
            if count3[i]<=target and count3[i+1]>=target:
                return count3[i] if (target-count3[i])<(count3[i+1]-target) else count3[i+1]
                
 #查的AC版本
class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        num.sort()
        result = num[0] + num[1] + num[2] #先记下前三个的和，后续再分别比较
        for i in range(len(num) - 2):
            j, k = i+1, len(num) - 1
            while j < k:
                sum = num[i] + num[j] + num[k]
                if sum == target:
                    return sum
                
                if abs(sum - target) < abs(result - target):
                    result = sum
                
                if sum < target:  #喔，前面先给数组排序了，然后可以这样来判断
                    j += 1
                elif sum > target:
                    k -= 1
        return result
        
#根据上面的思想把自己的代码改了下，也设置了初始值，然后直接每次判断count3，就不用再记录到最后了
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        ans=nums[0]+nums[1]+nums[2]
        tmp=abs(ans-target)
        count2 = []
        for i in range(1,len(nums)):
            for x in count2:
                if abs((x+nums[i])-target)<tmp:
                    ans=x+nums[i]
                    tmp=abs(ans-target)
            for x in nums[:i]:
                count2.append(x+nums[i])
        return ans
        #多么简洁呀！然后在289的时候又超时了..
       
