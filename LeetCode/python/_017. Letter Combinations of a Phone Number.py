class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        if '' == digits: return []
        kvmaps = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        return reduce(lambda acc, digit: [x + y for x in acc for y in kvmaps[digit]], digits, [''])
        
        #reduce()函数接收的参数和 map()类似，一个函数 f，一个list，
        #但行为和 map()不同，reduce()传入的函数 f 必须接收两个参数，
        #reduce()对list的每个元素反复调用函数f，并返回最终结果值。
