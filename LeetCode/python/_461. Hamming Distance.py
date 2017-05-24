#第一想法是都转为2进制字符串了比较，但想想应该有更快的，比如什么算差之类的
#好吧，查了个一行的。，还是转2进制，不过利用python 的库，bin()转后还是字符串的格式
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return bin(x^y).count('1')
