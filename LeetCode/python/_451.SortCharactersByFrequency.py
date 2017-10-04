#查了下python一行就搞定...
#这种类型很常见，就是需要统计两个东西，这里是字符及其出现次数
#看了一种优化方法：在统计完字符频率之后利用类似与计数排序的方法，开一个n+1长度大小的数组，将不同的频率字符放到频率的索引处．
#然后从高到低取得所有字符串．这种方法的好处是在最环情况下依然可以保证时间复杂度为O(n)．
#这里显然直接用了python库

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ''.join(c * t for c, t in collections.Counter(s).most_common())
        
        #出现次数可以用乘法
        #计数器（Counter）是一个容器，用来跟踪值出现了多少次。输出为一个键值对的字典（无序）
        #most_common()可以提取出最常用的。按键值对大小输出一个list（有序），每个元素为一个()元组
