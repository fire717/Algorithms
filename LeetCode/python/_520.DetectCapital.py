'''
查了下python判断字符串
s.isalnum() #所有字符都是数字或者字母
s.isalpha() #所有字符都是字母
s.isdigit() #所有字符都是数字
s.islower() #所有字符都是小写
s.isupper() #所有字符都是大写
s.istitle() #所有单词都是首字母大写，像标题
s.isspace() #所有字符都是空白字符、\t、\n
'''
#49ms-73%
class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word.isupper() or word.islower() :
            return True
        if word[1:].islower():
            return True
        return False
