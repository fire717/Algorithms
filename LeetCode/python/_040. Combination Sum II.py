# dp
#这里不是很懂
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        table = [None] + [set() for i in range(target)]
        #输出table=[None,set([])...target个...]
        for i in candidates:
            if i > target:
                break
            for j in range(target - i, 0, -1):
                table[i + j] |= {elt + (i,) for elt in table[j]}
            table[i].add((i,))
            #set.add给集合添加元素 / 给前面初始的set([])填入，得到set([(i,)])
        return map(list, table[target])
        #map(function, iterable)对可迭代函数'iterable'中的每一个元素应用‘function’方法，将结果作为list返回。
