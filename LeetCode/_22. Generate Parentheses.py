# 算打卡吧..

class Solution:  
    # @param {integer} n  
    # @return {string[]}  
    def generateParenthesis(self, n):  
        res=[]  
        tmp=['' for i in range(n+n)]  
        self.generate(res,n,n,tmp,0)  
        return res  
    def generate(self,res,l,r,tmp,index):  
        if l==0 and r==0:  
            res.append(''.join(tmp))  
            return  
        if l>0:  
            tmp[index]='('  
            self.generate(res,l-1,r,tmp,index+1)  
        if r>0 and r>l:  
            tmp[index]=')'  
            self.generate(res,l,r-1,tmp,index+1)  
