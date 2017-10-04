# 哈我这算法95ms居然超过 90%的人，不过肯定不是常规解法（虽然我并不知道）...基于python的比较特殊的解法吧

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        for x in ransomNote:
            if x not in magazine:
                return False
            else:
                magazine = magazine.replace(x,'',1)  
                #返回字符串中的 old（旧字符串） 替换成 new(新字符串)后生成的新字符串，如果指定第三个参数max，则替换不超过 max 次。
                #自己灵机一动，想到返回的再赋值，结果AC了
        return True
