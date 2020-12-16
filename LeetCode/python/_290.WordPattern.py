# 虽然是自己写自己调试的，但是参考了别人的思路，说是什么集合论双射，先打上_吧。35ms，超过93%。

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        ss = str.split(' ')
        if len(pattern)!=len(ss):
            return False
        t= {}
        for i in range(0,len(ss)):
            if pattern[i] not in t:
                t[pattern[i]]=ss[i]
            else:
                if t[pattern[i]]!=ss[i]:
                    return False
        tkey = []
        for i in t:
            if t[i] not in tkey:
                tkey.append(t[i])
            else:
                return False
        return True

    
    ######## 时隔4年，这次没half自己做出来了， 但是效率低一些  
    # 35ms -> 44ms， 还多了14mb内存占用...（看了下代码差不多，list还换成set了，可能是因为4年前没统计内存占用）
    ## 果然 重新提交了一下上面得方案，时间和内存一样了，但是只超过34%速度和5%内存了...
    class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        str_list = s.split(' ')
        count = len(pattern)
        if count != len(str_list):
            return False
        
        map_dict = {}
        value_set = set([])
        for i in range(count):
            # print(i)
            if pattern[i] not in map_dict:
                if str_list[i] in value_set:
                    return False
                # print(pattern[i], str_list[i])
                map_dict[pattern[i]] = str_list[i]
                value_set.add(str_list[i])
                #print(value_set)
            else:
                # print(map_dict[pattern[i]], str_list[i])
                if  map_dict[pattern[i]] != str_list[i]:
                    return False

        return True
    
#看了下官方解法：就是用两个词典存储嘛。。。
# 36ms，14mb内存，超过79%速度和5%内存
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word2ch = dict()
        ch2word = dict()
        words = s.split()
        if len(pattern) != len(words):
            return False
        
        for ch, word in zip(pattern, words):
            if (word in word2ch and word2ch[word] != ch) or (ch in ch2word and ch2word[ch] != word):
                return False
            word2ch[word] = ch
            ch2word[ch] = word
    
        return True
    
