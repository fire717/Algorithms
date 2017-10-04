#这次是完全没思路，算是第一次算是自然语义处理的
#一开始是想分析每个数字的子母，从唯一的字母入手，但是很少
#好吧，网上查的思路：找到每个数字独一无二的字母，让其唯一代表该数字，如果没有，尽量找到这样的字母，它代表的数字尽可能少，且仅出现一次。
#类似，但是都是其他语言写的，然后论坛找了个简洁的python解法，用到了计数器，具体实现还是有点不懂
#collections.Counter(x)用于把字符串x中所有字符统计出现的次数以字典返回

class Solution(object):
    def originalDigits(self, s):
        numbers = [('zero',0),('two',2),('eight',8),('four',4),('one',1),('three',3),('five',5),('six',6),('seven',7),('nine',9)]
        res, S = [], collections.Counter(s)
        for n in numbers:
            c = collections.Counter(n[0])
            while c&S == c:
                res.append(n[1])
                S -= c
        return ''.join([str(i) for i in sorted(res)])
