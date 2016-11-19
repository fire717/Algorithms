# 试了下直接操作，发现str不能位运算。剩下的思路只有转换为10进制再转回2进制，肯定超时
# 好吧突然想起直接int(str)可以了，继续去试试
# 没试出来..想起分别用异或保存和、与保存进位，但是后面不知道怎么处理了，好像要用循环

# 一.python直接可以进制转换。。。
class Solution(object):
    def addBinary(self, a, b):
        return bin(int(a, 2) + int(b, 2))[2:]

#二 从两个字符串的最低位开始，一位一位的进行二进制相加，并保存进位，最终可以得到两者的和的字符串。
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res = ''
        i, j, plus = len(a)-1, len(b)-1, 0
        while i>=0 or j>=0 or plus==1:
            plus += int(a[i]) if i>= 0 else 0
            plus += int(b[j]) if j>= 0 else 0
            res = str(plus % 2) + res
            i, j, plus = i-1, j-1, plus/2                #三个变量同时赋值
        return res
