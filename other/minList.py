#coding:utf-8
#by Fire / 2018.9.11
#返回数组中和最小的子数组

s0 = [1,2,3,-3,2,-10,3] #[-10]
s1 = [1,2,3,-2,3,-10,3] 
s2 = [1,2,3]
s3 = [1,-3,5]

def findClear(new_list):
    #print(new_list)
    l = len(new_list)
    tmp = new_list[0]
    start = 0
    end =  1
    for i in range(1,l):
        if new_list[i]+tmp>=0:
            tmp=new_list[i+1]
            start = i+1
            end = i+2
        else:
            tmp+=new_list[i]
            end +=1

    return new_list[:start],new_list[start:end+1],new_list[end+1:]

def test_func2(num_list):
    '''
    求数组中最大子序列的乘积，子序列必须连续
    '''
    l=len(num_list)
    left = 0
    hasNone = 0
    flag = 0
    flag_left = 0
    for i in range(l):
        if num_list[i]<0:
            hasNone = 1
            if flag==0:
                left = i
                flag = 1
            right = i
    if hasNone==0:
        return num_list,[],[]
    else:
        if left==right:
            return num_list[:left],num_list[left:left+1],num_list[left+1:]
        else:
            new_list = num_list[left:right+1]
            L,M,R = findClear(new_list)
            L = num_list[:left]+L
            R = R+num_list[right+1:]
            return L,M,R

print(test_func2(s0))
print(test_func2(s1))
print(test_func2(s2))
print(test_func2(s3))
