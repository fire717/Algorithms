#59ms-10%
#唉一个easy都调了几次才AC，还这么慢，写的还这么多...
class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        alphabet = ['qwertyuiopQWERTYUIOP','asdfghjklASDFGHJKL','zxcvbnmZXCVBNM'] #要考虑大写
        ans = []
        for x in xrange(len(words)):
            lw = len(words[x])
            if lw == 1: #要考虑单个字母
                ans.append(words[x])
                continue  #这不是break
                
            for i in xrange(3):  #先找出在那一行
                if words[x][0] in alphabet[i]:
                    row = i
                    break

            for j in xrange(1,lw):
                if words[x][j] not in alphabet[i]:
                    break
                if j == len(words[x]) - 1:
                    ans.append(words[x])
        return ans
