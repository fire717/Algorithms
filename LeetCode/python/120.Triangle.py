#终于等到你！
#一开始想的很简单，结果提交时报错，一看，发现不是简单的选每一行最小的，而是总和最小...那就又是dp了！赶紧练一下。
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        sum = triangle[0][0]
        j=0
        for i,n in enumerate(triangle):
            try:
                if triangle[i+1][j] > triangle[i+1][j+1]:
                    sum += triangle[i+1][j+1]
                    j = j+1
                else:
                    sum += triangle[i+1][j]
            except:
                return sum
                
   


#好吧，还是自己做出来的。但是好像没用到dp的思想..没用逆序，而是从第一层开始算，只是用了个字典记录，不重复计算。
#才68ms-27%...写的也很丑...
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        sum = {} #记录到每一层的最短和,从0计数吧,(a,b):c的格式，a代表层数，b代表列的位置，c代表和
        l = len(triangle)
        if l == 0:return 0
        if l == 1:return triangle[0][0]
        if l == 2:return min(triangle[0][0]+triangle[1][0],triangle[0][0]+triangle[1][1])
        sum[(0,0)]=triangle[0][0]
        sum[(1,0)]=triangle[1][0]
        sum[(1,1)]=triangle[1][1]
        for i in xrange(1,l):
            sum[(i,0)] = sum[(i-1,0)] + triangle[i][0]
            sum[(i,i)] = sum[(i-1,i-1)] + triangle[i][i]
            for j in xrange(1,i):
                t1 = sum[(i-1,j-1)] + triangle[i][j]
                t2 = sum[(i-1,j)] + triangle[i][j]
                sum[(i,j)]=min(t1,t2)
        ans = []
        for i in xrange(l):
            ans.append(sum[(l-1,i)])
        return min(ans)
        
        


#有空在想怎么优化吧...
#顺便先放个别人的写法
#查了几个..一个69ms，一个80多ms...
#就放个这个简介的吧，也是从下到上的

class Solution(object):
    # bottom-up, O(n) space
    def minimumTotal(self, triangle):
        if not triangle:   #可以这样判断是否为空
            return 
        res = triangle[-1]
        for i in xrange(len(triangle)-2, -1, -1):
            for j in xrange(len(triangle[i])):
                res[j] = min(res[j], res[j+1]) + triangle[i][j]
        return res[0]
