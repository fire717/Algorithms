# 字符串处理真是麻烦，不能像list那样直接y通过索引赋值。一开始想通过s[i:1]来赋值，也不行，然后想到了replace()，但是判断重复很麻烦
# 然后想到了直接生成新的字符串，通过了几个测试，结果提交超时了...
# 我的超时解法
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        v = ['a','e','i','o','u','A','E','I','O','U']
        j=1
        l=len(s)
        ans = ''
        vs=''
        for i in xrange(0,l):
            if s[i] in v:
                vs+=s[i]
        for i in xrange(0,l):
            if s[i] not in v:
                ans+=s[i]
            else:
                ans+=vs[-j]
                j+=1
        return ans
        
# 查的一个解法
# 呵呵 ，就是把字符串转为列表再转回字符串.....
class Solution(object):
    def reverseVowels(self, s):
        res = list(s)                     #！！！！！！！这里，字符串转list  
        vowels = ['a', 'e', 'i', 'o', 'u']
        start = 0; end = len(s) - 1
        while start < end:
            while start < end and (s[start].lower() not in vowels):
                start += 1
            while start < end and (s[end].lower() not in vowels):       
                end -= 1
            if(start != end):
                tmp = res[start]
                res[start] = res[end]
                res[end] = tmp
            start += 1; end -= 1
        return ''.join(res)            #转回去比较熟悉
