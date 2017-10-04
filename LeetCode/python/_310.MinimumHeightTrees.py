#比较慢
class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        d = collections.defaultdict(set) #生成无重复值的字典
        for u, v in edges: #每次取边的两节点
            d[u].add(v)
            d[v].add(u)
        s = set(range(n))#生成一个0到n-1的集合
        while len(s) > 2: 
            leaves = set(i for i in s if len(d[i]) == 1)   #每次减去叶节点，到剩余两个为止（只会有两个或者1个节点）
            s -= leaves
            for i in leaves:
                for j in d[i]:
                    d[j].remove(i)
        return list(s)
