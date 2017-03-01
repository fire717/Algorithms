# 埃拉托斯特尼筛法/厄拉多塞筛法
# 下面这个是改的百度百科的，写的好烂...
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<3:
            return 0
        f = []
        for i in range(n+1):
            if i > 2 and i%2 == 0:
                f.append(1)
            else:
                f.append(0)
        i = 3
        while i*i <= n:
            if f[i] == 0:
                j = i*i
                while j <= n:
                    f[j] = 1
                    j += i+i
            i += 2
        p = 1
        for x in range(3,n,2):
            if f[x] == 0:
                p+=1
        return p
