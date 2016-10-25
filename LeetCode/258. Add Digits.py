# 开始没分清x和num搞了半天，果然还是不熟悉T.T。然后一直return none 最终解决了，又学到一个知识点
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        x = 0
        if num >= 10:
            while num >= 1:
                x = x+num%10
                num = num/10
            return self.addDigits(x)       #就是这里！要记住，递归函数也要加return，不然就会返回none
        else:
            return num
