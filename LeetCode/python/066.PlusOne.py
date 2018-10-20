# 读不懂题目...
# 查了下L：【题意】 给你一个用数组表示的数，求加一之后的结果，结果还是用数组表示。 【分析】 从低位到高位，连续遇到9才能加一进位。
# 还是TM不懂啊....
# 额 试了几个大概懂了，就是以【列表】形式表示【一个】数字的不同位数...毛线个数组
# 还是不难，懂了之后很快就写出来了，算是比较简洁，不过速度一般，45ms-77%
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        ans = [0]
        if digits.count(9)==len(digits):
            ans =  [0 for i in xrange(len(digits)+1)]   #熟悉重复list的生成
            ans[0]=1
        else:
            for i in range(1,len(digits)+1):
                if digits[-i]!=9:
                    digits[-i] = digits[-i]+1
                    ans = digits
                    break
                else:
                    digits[-i] = 0
        return ans

    
 # 2018.10.20  云天励飞远程面试
# 忘了上面n久前的解法，第一思路是转str再转数字再转回来 ，但觉得面试这么写多半不行，于是写了下面：
# 24 ms - 99.81%
class Solution:
    def plusOne(self, nums):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        l = len(nums)
        foreward = 1
        for i in range(1,l+1):
            if nums[-i]+foreward==10:
                nums[-i] = 0
                foreward = 1
            else:
                nums[-i] += 1
                foreward = 0
                break
        if foreward == 1:
            nums = [1] + nums
        return nums

#然后事后查了下网上的解法，就是转字符串的，28ms-88.6%  .
#明显我的解法更优，但是面试官没任何评价直接就结束了，让我很慌...
class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        intNum = 0
        for i in range(len(digits)):
            intNum = intNum * 10 + digits[i]
        intNum += 1
        # 数字转换成字符
        strNum = str(intNum)
        # 字符转换成数组
        res = []
        for i in range(len(strNum)):
            res.append(int(strNum[i]))
        return res

