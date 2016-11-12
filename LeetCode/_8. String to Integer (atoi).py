# 题目本身不难。就是各种特殊情况很复杂 ，而且我也没搞懂"1+1"输出1，"+-1"输出0，"+1"输出1...

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        INT_MAX=2147483647;INT_MIN=-2147483648  
        index=0  
        while index<len(str) and str[index]==' ':index+=1  
        flag=1  
        if index<len(str) and str[index]=='-':  
            index+=1  
            flag=-1  
        elif index<len(str) and str[index]=='+':  
            index+=1  
        res=0  
        while index<len(str):  
            if str[index]<'0' or str[index]>'9':return flag*res  
            digit=ord(str[index])-ord('0')  
            if flag==1 and res*10+digit>INT_MAX:return INT_MAX  
            if flag==-1 and res*10+digit>-INT_MIN:return INT_MIN  
            res=res*10+digit  
            index+=1  
        return flag*res
