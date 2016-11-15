#题目又乱说，明明返回应该是List[int]，又说是rtype: int，这不误导人吗？！
# 这样写不知道哪错了，说Line 54: TypeError: range() integer end argument expected, got list.
# 我既没有54行，也没有用range，也没有使用第三方库，不知道为啥错....
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<2:
            return nums
        l = len(nums)-1
        i = 1
        while i<=l:                  #这种上限在变得循环就不能用for 只能用while了
            if nums[i]==nums[i-1]:
                nums.pop(i)
                l-=1
            else:
                i+=1
        return nums
# 呵呵呵呵呵，我就说题目出错了，就该是返回int...例子里的输出又非得是[]输出的...
# return len(nums)就好了....

#额，速度有点慢，149ms-13%
        
