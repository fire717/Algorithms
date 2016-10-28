# 感觉自己对str处理沉迷replace(x,'',1)不能自拔了，简单粗暴好用，只是这个时间复杂度...800ms，超过0.4%的人...
# 恩，python还是先讲实现，后面学C再慢慢注重效率吧

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        for x in s:
            if x in t:
                t = t.replace(x,'',1)
            else:return False
        if len(t) != 0:
            return False
        else:return True
