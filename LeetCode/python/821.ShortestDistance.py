# 88ms 56%
class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        reS = S[::-1]
        fore_dis = []
        back_dis = []
        l = len(S)
        for i in range(l):
            f = S[i:].find(C)
            fore_dis.append(f if f>=0 else 10000)
            b = reS[i:].find(C)
            back_dis.append(b if b>=0 else 10000)
        res = []
        print(fore_dis, back_dis)
        for j in range(l):
            res.append(min(fore_dis[j], back_dis[-j-1]))
        return res
            
