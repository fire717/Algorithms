# 感觉算法不难，就是凑输出格式比较麻烦
# 还是DFS
# 这种有额外东西的迭代，内部再搞一个函数...
class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        paths=[]  
        if root is None:  
            return paths  
        def add(root,tList):    #Note that memory copy  
            tList.append(root.val)  
            status=1  
            if root.left:  
                lList=tList[:]    #deep copy  
                add(root.left,lList)  
                status=0  
            if root.right:  
                rList=tList[:]  
                add(root.right,rList)  
                status=0  
            if status:  
                paths.append("->".join([str(t) for t in tList]))         #熟悉下join
        add(root,[])  
        return paths  
