#直接ac，遍历了两次
#262ms-8%......好像是最低的一次//后面再改进吧
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        tmpI = []
        tmpJ = []
        for i in xrange(len(matrix)):
            for j in xrange(len(matrix[i])):
                if matrix[i][j] == 0:
                    tmpI.append(i)
                    tmpJ.append(j)
        for i in xrange(len(matrix)):
            for j in xrange(len(matrix[i])):
                if i in tmpI or j in tmpJ:
                    matrix[i][j] = 0
