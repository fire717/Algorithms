#一开始想到了数字非1位，但没有考虑到"3[a2[c]]"这种情况，那就要递归了...
class Solution(object):
    def singleStr():
        
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans=''
        i=0
        while i < len(s):
            t=''
            t2=''
            while s[i] != '[':
                t+=s[i]
                i+=1
            i+=1
            while s[i] != ']':
                t2+=s[i]
                i+=1
            ans+=t2*int(t)
            i+=1
        return ans
#chade...
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        k = 1
        parts = collections.defaultdict(str)
        digits = collections.defaultdict(int)
        for c in s:
            if c.isdigit():
                digits[k] = digits[k] * 10 + int(c)
            elif c == '[':
                k += 1
            elif c == ']':
                parts[k - 1] += digits[k - 1] * parts[k]
                digits[k - 1] = 0
                parts[k] = ''
                k -= 1
            else:
                parts[k] += c
        return parts[1]
