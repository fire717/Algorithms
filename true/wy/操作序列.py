"""
小易有一个长度为n的整数序列,a_1,...,a_n。然后考虑在一个空序列b上进行n次以下操作:
1、将a_i放入b序列的末尾
2、逆置b序列
小易需要你计算输出操作n次之后的b序列。 

思路：找规律
"""

x1 = input()
x2 = input()

x2_list = x2.split(' ')
ans = []
l = int(x1)
i = l-1
while i>=0:
    ans.append(x2_list[i])
    i-=2
i = l%2
while i<l:
    ans.append(x2_list[i])
    i+=2
print(' '.join(ans))
