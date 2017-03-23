# 没思路...
# 想到有可能用dp，但也不知道怎么操作
# 查了下有很多种解法，可以dp，可以bfs，这是bfs

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return n
        lst = []
        i = 1
        while i * i <= n:
            lst.append( i * i )
            i += 1      #先找出所有小于n的平方数，加入列表
        cnt = 0
        toCheck = {n}
        while toCheck:
            cnt += 1
            temp = set()
            for x in toCheck: #对要继续细分的数
                for y in lst: #对每个平方数
                    if x == y: #相等直接返回
                        return cnt
                    if x < y: #小于就跳出本层  / 因为是bfs
                        break
                    temp.add(x-y)#集合用add. / 一轮下来，保存了本层的所有分支节点值
            toCheck = temp

        return cnt
