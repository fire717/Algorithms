# 知道用bfs，但是就是不知道怎么写，写不知道如何判断是新的一层...学习...

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        depth = 0
        q = [root]
        while len(q) != 0:
            depth += 1                            #每个while中遍历完一层
            for i in range(0, len(q)):                   #for循环控制一层队列
                if not q[0].left and not q[0].right:
                    return depth
                if q[0].left:
                    q.append(q[0].left)
                if q[0].right:
                    q.append(q[0].right)
                del q[0]                         #用del 删除列表中元素，无d返回值
        return depth

#深度优先搜索（DFS），用递归求解。
"""
执行用时：
48 ms
, 在所有 Python3 提交中击败了
95.56%
的用户
内存消耗：
15.5 MB
, 在所有 Python3 提交中击败了
51.84%
的用户
"""
#注意，一个节点的最小高度不一定是两个子树的最小高度中较小的，当一个子树为空时，该节点的最小高度等于另一个子树的最小高度。
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0

        if not root.left:
            return 1 + self.minDepth(root.right)
        elif not root.right:
            return 1 + self.minDepth(root.left)
        else:
            return 1 + min(self.minDepth(root.left), self.minDepth(root.right))

        
#2020.8.21
"""
执行用时：
52 ms
, 在所有 Python3 提交中击败了
88.03%
的用户
内存消耗：
14.8 MB
, 在所有 Python3 提交中击败了
89.71%
的用户
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        node_queue = [root]
        next_layer = []
        depth = 1
        while 1:

            while len(node_queue)>0:
                flag = 0
                if node_queue[0].left:
                    next_layer.append(node_queue[0].left)
                    flag+=1
                if node_queue[0].right:
                    flag+=1
                    next_layer.append(node_queue[0].right)
                if flag==0:
                    return depth

                node_queue = node_queue[1:]
            if len(next_layer)>0:
                depth+=1
                node_queue = next_layer
