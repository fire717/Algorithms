# 虽然是自己写自己调试的，但是参考了别人的思路，要考虑双射，先打上_吧。35ms，超过93%。

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        ss = str.split(' ')
        if len(pattern)!=len(ss):
            return False
        t= {}
        for i in range(0,len(ss)):
            if pattern[i] not in t:
                t[pattern[i]]=ss[i]
            else:
                if t[pattern[i]]!=ss[i]:
                    return False
        tkey = []
        for i in t:
            if t[i] not in tkey:
                tkey.append(t[i])
            else:
                return False
        return True
