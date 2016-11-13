# 一开始一直错，生成数组长度都一样，终于发现原因了..
# [[]]是一个含有一个空列表元素的列表,所以[[]]*3表示3个指向这个空列表元素的引用,修改任何一个元素都会改变整个列表:
# 应该这样创建多维数组：lists = [[] for i in range(3)]
# 改了果然可以了，c双重循环都能超过88%（36ms）..

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ans = [[] for i in range(numRows)]                         #关键！
        for i in xrange(0,numRows):
            for j in xrange(0,i+1):
                if j==0 or j==i:
                    ans[i].append(1)
                else:
                    ans[i].append(ans[i-1][j-1]+ans[i-1][j])
        return ans
