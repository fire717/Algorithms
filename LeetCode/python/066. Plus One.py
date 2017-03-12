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
