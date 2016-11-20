#开始没看懂题，看了测试才知道，原来是求第n个，没找出规律...

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        seq=['1'];top=1;  
        while n-1>0:  
            n-=1;index=0;bak=[]  
            i=0  
            while i<top:  
                num=1  
                while i+1<top and seq[i+1]==seq[i]:i+=1;num+=1  
                bak.append(chr(num+ord('0')))   #这个不错
                bak.append(seq[i])  
                i+=1  
            seq=bak;top=len(bak)  
        return ''.join(seq)  
