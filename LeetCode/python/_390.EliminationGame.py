#按正常思路做下来，在5428超时了。
#估计又要用到什么数学方法
class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1:return 1
        ans = [x for x in range(1,n+1) if x%2==0] #判断了n>1后，通过列表推导式直接生成第二步的
        sidet = 1 #记录方向，0从左，1从右
        while len(ans)>1:
            tmp = len(ans)
            if sidet == 1:
                for i in range(tmp):
                    if i%2 == 0:
                        ans.pop(tmp-1-i)
                sidet = 0
            else:
                countpop = 0
                for i in range(tmp):
                    if i%2 == 0:
                        ans.pop(i-countpop)
                        countpop += 1
                sidet = 1  
        return ans[0]
        
 
 #AC版本
 #不看做左右，而是当做一个循环圈
 #即4个一组一循环，后面的就当成迭代
 class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 3 or n == 2:
            return 2
        elif n == 1:
            return 1
        else:
            base = 4 * self.lastRemaining(n/4)   
            if n%4 == 0 or n%4 == 1:
                return base - 2
            else:
                return base
