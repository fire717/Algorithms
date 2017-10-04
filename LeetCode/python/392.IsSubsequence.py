#感觉好久没有自己AC了...这个又简洁，还72ms  94%
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        for x in s:
            if x in t:
                t=t[t.find(x)+1:]    #主要就是这个方法。str.find('x')，返回字符串中第一个匹配x的字符的index
            else:
                return False
        return True

#想着改进下，把if判断换成t.find(x)>=0，结果时间变成92ms了，看来if x in str比str.find()效率要高一点
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        for x in s:
            if t.find(x)>=0:
                t=t[t.find(x)+1:]
            else:
                return False
        return True
