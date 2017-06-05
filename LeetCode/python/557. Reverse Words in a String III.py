#一次性AC，只是 149 ms-18%..
lass Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        t =s.split()
        ans = ''
        for str in t:
            ans=ans+str[::-1]+' '
        return ans[:-1]
