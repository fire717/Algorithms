#以为数字数量是固定的，很好解，然后才发现是k个数字，没头绪了
#查了下，说是回溯法。

class Solution(object):
    def solve(self,k,cur,remainder,prevVal,listT,result):
        if cur == k:
            if remainder > prevVal and remainder <= 9:
                listT.append(remainder)
                one = listT[:]
                result.append(one)
                del listT[-1]
        elif cur < k:
            for i in range(prevVal+1,9-(k-cur)+1):
                listT.append(i)
                self.solve(k, cur+1,remainder-i, i ,listT,result)
                del listT[-1] 

    def combinationSum3(self, k, n):
        result = []
        listT = []
        if k > 0 and k <=9:
            self.solve(k,1,n,0,listT,result)
        return result
