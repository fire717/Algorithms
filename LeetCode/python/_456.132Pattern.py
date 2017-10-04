#最简单想法，三重循环，果然超时了（那你还试...）
class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        l = len(nums)
        for i in xrange(l-2):
            for j in xrange(i+1,l-1):
                for k in xrange(j+1,l):
                    if nums[i] < nums[k] and nums[k] < nums[j]:
                        return True
        return False
        
        
 #改进下，从第一个数开始，找第一个比他大的，再记录范围，往后依次判断是否在
 #当不存在时，再继续往后.
 #试了下，还是不可行..
 
 #查的..用的栈，O(n)复杂度
class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(set(nums)) < 3:
            return False
        stack = [[nums[0], nums[0]]]  #这样保持 厉害了啊
        current_min = nums[0]
        for i in range(1, len(nums)):
            curr = nums[i]
            if curr >= stack[0][1]:  # curr >= max(nums[:i])
                stack = [[current_min, curr]]
            elif curr < current_min:  # curr < min(nums[:i])
                stack.append([curr, curr])
                current_min = curr
            elif curr == current_min:
                continue
            else:
                while stack and curr > stack[-1][0]:
                    if curr < stack[-1][1]:
                        return True
                    else:
                        stack.pop()
                stack.append([current_min, curr]) #pop了在添加
        return False
 
