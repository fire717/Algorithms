#实现不难，但是线性+无额外空间，还是有点挑战
#好吧 没思路...查了下 要位运算
#分别记录出现次数，最后返回出现一次的。
#使用三个变量one、two、three来存储【每一个位】上出现的1、2、3次的情况
#python位运算可直接运算，不需要进行进制转换

class Solution(object):
    def singleNumber(self, nums):
        one = 0
        two = 0
        three = 0
        for i in range(0,len(nums)):
            two |= one & nums[i] #当新来的为0时，two = two | 0，two不变，当新来的为1时，（当one此时为0，则two = two|0，two不变；当one此时为1时，则two = two | 1，two变为1
            one ^= nums[i]       #新来的为0，one不变，新来为1时，one是0、1交替改变
            three = one & two    #当one和two为1是，three为1（此时代表要把one和two清零了）
            one &= ~three        #把one清0
            two &= ~three        #把two清0
        return one



