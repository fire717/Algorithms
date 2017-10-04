# 这些真的是easy难度吗...
# 一开始想到位运算，但没细想怎么处理进位，然后百度了下得到一个解法 ：

class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        while b:
            x = a^b
            y = (a&b) << 1          #这里注意下位移运算 优先级高于位运算
            a = x
            b = y
        return a
        
# 测试没问题，但提交又报错了，原因是计算不了-1然后超时报错了
# 再次直接百度python解法。
# 报错原因：由于【Python没有无符号右移操作】，并且当左移操作的结果超过最大整数范围时，会自动将int类型转换为long类型，因此需要对上述代码进行调整。

class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        MAX_INT = 0x7FFFFFFF
        MIN_INT = 0x80000000
        MASK = 0x100000000
        while b:
            a, b = (a ^ b) % MASK, ((a & b) << 1) % MASK
        return a if a <= MAX_INT else ~((a % MIN_INT) ^ MAX_INT)  #负数先与最大正数异或再取反，因为为1的位会进位成0
