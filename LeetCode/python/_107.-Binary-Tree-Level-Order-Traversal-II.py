# 用两个列表，一个当做队列暂存当前的节点，一个作文输出结果

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root==None:
            return []
        resultslist=[[root.val]]
        currootlist=[root]
        
        while True:
            resultstmplist=[]
            curtmplist=[]
            for i in range(0,len(currootlist)):
                cur=currootlist[i]
                if cur.left!=None:
                    curtmplist.append(cur.left)
                    resultstmplist.append(cur.left.val)
                if cur.right!=None:
                    curtmplist.append(cur.right)
                    resultstmplist.append(cur.right.val)
            
            if len(curtmplist)==0:
                break
            resultslist.append(resultstmplist)
            currootlist=curtmplist
            
        resultslist.reverse()    
        return resultslist
