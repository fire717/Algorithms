# 这题的主要特点是要观察出新序列的位置为 2*numRows-2

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows==1 or len(s)<=1:  
            return s  
        n=numRows  
        size=2*n-2  
        result=[]  
        for i in range(n):  
            j=i  
            while j<len(s):  
                result.append(s[j])  
                if i!=0 and i!=n-1 and j+size-2*i<len(s):  
                    result.append(s[j+size-2*i])  
                j+=size  
        return "".join(result)  
                
