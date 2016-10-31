# 超过90%多的人，是我取巧了吗...eval真的好用啊

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        tem='%d' %eval(num1+'+'+num2)
        return tem
