#感觉不怎么难，但是有点读不懂题目...比如例子中的前6个元素为什么只取了前5个“12211”
#好吧，理解简单所以才想错...原来是没有规律的
'''
字符串模拟
令魔法字符串ms = '122'，维护指针p，初始令p = 2
若ms[p] == '1' 则向ms追加1个与ms末尾元素不同的字符
否则，向ms追加2个与ms末尾元素不同的字符
'''
class Solution(object):
    def magicalString(self, n):
        """
        :type n: int
        :rtype: int
        """
        ms = '122'
        p = 2
        while len(ms) < n:
            ms += str(3 - int(ms[-1])) * int(ms[p])
            p += 1
        return ms[:n].count('1')
