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

'''
理解：
传入参数

k与cur：两个用来比较判断递归的层次，如果cur当前层已经等于k了，那么就代表是最后一层了，要对result集进行操作了。
remainder与prevVal：prevVal代表当前选取了的数字，有两个作用，和remainder比较，用来判断是否需要添加remainder到list（如果remainder < prevVal，即我选了8，剩下了3,，那还怎么选，因为我只有一个9了）。
list ：list作为回溯的主角，每次尝试append一个值之后，在下层递归后，要删除最后一个元素，保留原始状态（并不关系递归里面的结果，只关系当前状态）
'''
