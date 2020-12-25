"""
#https://leetcode-cn.com/problems/count-sorted-vowel-strings/solution/yi-ci-zai-kai-tou-zeng-jia-zi-mu-by-joys-ls41/
n=1 的情况，为['a','e','i','o','u']
res 数组记录n-1时以对应字母结尾的字符的个数

比如n=3 时res[4] 为1,表示n=2有1个元素开头为'u',那么在这一步，可以在这个元素的基础上，在最前面增加'u'
此时，可以增加'o'的元素为res[0]+res[1],即n=2时开头为'o'与'u'的元素，
以此类推。


"""
class Solution:
    def countVowelStrings(self, n: int) -> int:
        if n==1:
            return 5
        res=[1,1,1,1,1]
        for i in range(0,n-1):
            for j in range(4,0,-1):
                res[j]=sum(res[0:j+1])
        return sum(res)
