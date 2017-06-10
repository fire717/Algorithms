#test几下然后一次性AC
#虽然思想很暴力...
#135ms-21%...

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        v = []
        t = [root]
        while t:
            if t[0].left:
                t.append(t[0].left)
            if t[0].right:
                t.append(t[0].right)
            v.append(t[0].val)
            t=t[1:]
        v.sort()
        minV = 100000
        for i in xrange(len(v)-1):
            tmp = v[i+1]-v[i]
            if tmp<minV:
                minV = tmp
        return minV
