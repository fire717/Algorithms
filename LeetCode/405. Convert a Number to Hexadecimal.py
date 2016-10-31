# 这个算比较完美，调试了几次然后一次AC，时间39ms打败90%多人，也没用什么神奇的python方法...当然用了个字典class Solution(object):

class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        hex={10:'a',11:'b',12:'c',13:'d',14:'e',15:'f'}
        h = ''
        if num>0:
            while num:
                t = num%16
                if t<10:
                    h='%d' %t +h         # 这里领悟了字符串拼接的技巧，这样写就可以从首部插入了/也可以全部数字写进字典不过有点麻烦，就搞了一个if
                else:
                    h=hex[t]+h
                num/=16
            return h
        elif num<0:
            num = 16**8+num
            return self.toHex(num)    #相当于补码吧
        else:return "0"
