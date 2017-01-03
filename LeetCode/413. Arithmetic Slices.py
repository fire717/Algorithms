#终于自己搞定了一个有点难的题目~虽然才55ms-21%

class Solution(object):
    def conseq2count(self,n):                         #用这个函数来转换序列长度为对应的可组成Arithmetics数
        if n<3:                                       #自定义的类内函数要加一个self，不然一直报错说参数个数不对
            return 0
        else:
            return (1+n-3+1)*(n-3+1)/2
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        l = len(A)
        if l<3:
            return 0
        
        A.append(0)       #给A最后添加一个0防止不可中断（这里虽然AC了，但是觉得还是不够严谨，应该想其他的中断办法，比如长度）
        temp=[]           #记录间隔相等的连续的最长长度
        mid=A[1]-A[0]     #记录间隔值
        count=2

        for i in range(1,l):
            if A[i+1]-mid== A[i]:
                count+=1
            else:                      #间隔值变化时记录此时的count
                temp.append(count)
                count=2
                mid=A[i+1]-A[i]

        ans=0
        if temp:
            for x in temp:
                ans+=self.conseq2count(x)   #要加self
            return ans
        else:
            return 0
