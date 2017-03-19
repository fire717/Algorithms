#好吧是整体顺时针旋转90度..想成求对称了
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        l = len(matrix)
        for i in range(l):
            for j in range(i+1,l):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]

#应该是有某种规律，先怎么换再怎么换最后就可以转到90度
#恩..没有头绪的果断查了..
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for l in xrange(n / 2):
            r = n - 1 - l
            for p in xrange(l, r):
                q = n - 1 - p
                cache = matrix[l][p]
                matrix[l][p] = matrix[q][l]
                matrix[q][l] = matrix[r][q]
                matrix[r][q] = matrix[p][r]
                matrix[p][r] = cache
                #就相当于找出每个旋转的位置的变化情况，然后全部操作一遍，只是循环到n/2即可
                
#还有个只有一行的..不是很能看懂
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        matrix[::] = zip(*matrix[::-1])  #matrix[::-1]意思是把一级子列表逆序
        #查了下*都说是函数中接受多个参数，但是这里不是函数啊...
        #zip函数接受任意多个（包括0个和1个）序列作为参数，返回一个tuple列表。
