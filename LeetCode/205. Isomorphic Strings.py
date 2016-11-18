#调了好久。55 ms-90%
#主要是，理清几个关系：用字典保存出现过得子母，其值为出现的index，然后用list保存形状，相同的数字一样，不同的数字不同，把s和t都转换后来比较
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ss = {}
        tt = {}
        sn = []
        tn = []
        for i in xrange(len(s)):
            if s[i] not in ss:
                ss[s[i]]=i
            sn.append(ss[s[i]])
        for j in xrange(len(t)):
            if t[j] not in tt:
                tt[t[j]]=j
            tn.append(tt[t[j]])
        return sn==tn
