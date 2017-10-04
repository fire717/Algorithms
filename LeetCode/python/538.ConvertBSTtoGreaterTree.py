#恩，已经不怕树的遍历之类的问题了，虽然才 222 ms-6.20%..但也是自己做的。
#第二次刷时再优化吧

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root: #要单独考虑空树
            return []
        cache = [root] #遍历整个树
        n = [] #保存节点值
        while cache:
            n.append(cache[0].val)
            if cache[0].left:
                cache.append(cache[0].left)
            if cache[0].right:
                cache.append(cache[0].right)
            cache = cache[1:]
        n.sort(reverse=True)#降序
        t = {} #避免重复计算
        t[n[0]]=n[0]
        for i in xrange(1,len(n)):
            t[n[i]]=n[i] + t[n[i-1]]
        #第二次遍历 修改值
        cache = [root] #遍历整个树
        while cache:
            cache[0].val = t[cache[0].val]
            if cache[0].left:
                cache.append(cache[0].left)
            if cache[0].right:
                cache.append(cache[0].right)
            cache = cache[1:]
        return root
