#格雷码（相邻两数仅有一位二进制发生变化。）..没什么思路
#从最右边一位起，依次将每一位与左边一位异或(XOR)，作为对应格雷码该位的值，最左边一位不变(相当于左边是0)。
class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        resultCodeList = []
        for i in range(0,2 ** numLen):
            grayCode = (i >> 1)^i    #右移然后异或
            resultCodeList.append(grayCode)
        return resultCodeList
