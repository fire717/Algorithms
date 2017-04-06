class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        self.dfs(s, [], res)  
        return res

    def dfs(self, s, path, res): #递归
        if not s:
            res.append(path)
            return
        for i in range(1, len(s)+1):
            if self.isPal(s[:i]): #从头开始判断，因为前面也要满足
                self.dfs(s[i:], path+[s[:i]], res)#list可直接相加，不断添加回文。到上面判断s为空时添加

    def isPal(self, s): #逆序判断是否回文
        return s == s[::-1]
