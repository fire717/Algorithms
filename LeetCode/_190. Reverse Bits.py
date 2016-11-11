# 先将输入转换成2进制字符串，再翻转并扩充到32位，再将此32位的二进制转为无符号整数即可。利用Python的bin()函数很方便。
class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        b = bin(n)[:1:-1]                   #熟悉字符串处理技巧.[:1:-1]意思是逆序输出b[2]到b[n]
        return int(b + '0'*(32-len(b)), 2)           #int(a,b)a为要转换的数，b为a的进制数
