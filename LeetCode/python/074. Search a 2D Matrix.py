#思路好想，关键是要追求速度吧
#想到二分查找，也好写，但是又是各种边界条件调整了很久...
#后来干脆删了添加的。
#发现一个道理：不要一个test没通过就修修补补的加if什么的，要从算法本身去思考
#自己做出来的：52ms-42% 中规中距吧
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        l = len(matrix)
        #用二分查找吧
        bottom = 0
        top = l-1
        k = -1
        while matrix and bottom <= top:
            tmp = (bottom+top)/2
            if matrix[tmp] and tmp != k:
                if target in matrix[tmp]:
                    return True
                if target <matrix[tmp][0]:
                    top = tmp-1
                else:
                    bottom = tmp+1
                k = tmp
                continue
            top -= 1
        return False
