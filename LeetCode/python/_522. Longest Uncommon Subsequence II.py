'''
首先将输入字符串列表strs按照长度递减排序，记得到的新列表为slist。

利用计数器cnt统计每个字符串出现的次数。

遍历slist，记当前字符串为c，其下标为i：

    若c在strs中出现不止一次，跳过该字符串

    否则，利用贪心算法对c和slist[0 .. i - 1]的字符串进行匹配，若均匹配失败，则返回len(c)

遍历结束，返回-1
'''
class Solution(object):
    def uncommon(self, parent, child):
        lp, lc = len(parent), len(child)
        pp = pc = 0
        while pp < lp and pc < lc:
            if parent[pp] == child[pc]:
                pc += 1
            pp += 1
        return pc != lc
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        cnt = collections.Counter(strs)
        slist = sorted(set(strs), key=len, reverse=True)
        for i, c in enumerate(slist):
            if cnt[c] > 1: continue
            if all(self.uncommon(p, c) for p in slist[:i]):
                return len(c)
        return -1
