#发现了规律，每一斜的和都一样，这样就可以开始循环，然后通过奇偶判断方向即可
#测试中了小陷阱，循环时长度不是数组长度，因为是斜着的，应该是len*2-1。
#好吧这样一改也不行，对角线前后要分开来写..
#上限卡了会，结果写出x-m+l-x+m=l，额每日应！
#下面这个版本测试过了，结果提交时[[3],[2]]报错，原来不是方阵....
class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res=[]
        
        l=len(matrix)
        m=l-1
        
        for i in range(0,l):
            if i%2==0:
                for j in range(0,i+1):
                    res.append(matrix[i-j][j])
            else:
                for j in range(0,i+1):
                    res.append(matrix[j][i-j])
        for x in range(l,l*2-1):
            if x%2==0:
                for y in range(x-m,l):
                    res.append(matrix[x-y][y])
            else:
                for y in range(x-m,l):
                    res.append(matrix[y][x-y])
                
        return res
        
 ##############################################
 #好吧还是查了。就三行好简洁。
 class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        l = [[i,j] for i in range(len(matrix)) for j in range(len(matrix[0]))]   #学下并掌握这种写法啊
        l.sort(key=lambda x: float(x[0]+x[1])-float(x[(x[0]+x[1])%2])*0.00000001 ) #看不懂为啥用float什么的
        #sort中的key用于给sort提供排依据的函数，例如len()
        #lambda函数也叫匿名函数，即，函数没有具体的名称,而用def创建的方法是有名称的。
        return [matrix[x][y] for [x,y] in l] #这是按固定顺序返回吧
