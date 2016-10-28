# 没思路。百度学习了两种解法

#思路一
#分别统计s和t中每个字母出现的次数，不一样的即为所求。为了减少计算量，可以先遍历s，用数组统计26个字母出现的次数；再遍历t，在刚才的数组基础上对出现的字母次数减一，次数出现负数的字母即为所求。
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        letters = [0] * 26
        for c in s:
            letters[ord(c) - 97] += 1
        for c in t:
            letters[ord(c) - 97] -= 1
            if letters[ord(c) - 97] < 0:
                return c
                
#思路二
#考虑到t是由s添加一个字母得到，那么这个添加的字母在s和t中出现的总次数一定是唯一的一个奇数。基于这个想法，用异或操作得到该字母。
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        return chr(reduce(operator.xor, map(ord, s + t)))
