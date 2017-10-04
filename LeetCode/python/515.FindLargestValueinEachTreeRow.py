
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#思路好想，按照BFS遍历每一层，每次记录每层最大值
#但是就是不知道哪里错了测试就提示TLE..还是对树的操作不熟悉吧。还有就是对null这种判断不熟悉
#....多打了个字母，导致每次chache_son没有清空
#...改了之后就AC了。。。69 ms-98.99，比下面那个还快不少
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        cache_fa = [root]
        cache_son = []
        while cache_fa:#每次处理一层 
            tmp_max = cache_fa[0].val
            for i in cache_fa:
                if not i:
                    continue
                if i.val>tmp_max:
                    tmp_max = i.val
                if i.left:
                    cache_son.append(i.left)
                if i.right:
                    cache_son.append(i.right)
            ans.append(tmp_max)
            cache_fa = cache_son
            cache_son = []
        return ans
        
 #查了个看看
 class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        maxes = []
        row = [root]
        while any(row): #any(iterable)适用于2.5以上版本，兼容python3版本。
                        #如果iterable的任何元素不为0、''、False,all(iterable)返回True。如果iterable为空，返回False。
                        #这里要考虑任何元素不为0？
                        #应该是如果x=[null,null,...] 那么if row也是true的
            maxes.append(max(node.val for node in row))
            row = [kid for node in row for kid in (node.left, node.right) if kid] #推导式两层遍历...
            #先遍历row中每个节点，再遍历每个节点的两个子节点，再判断是否不为空，再添加
        return maxes
