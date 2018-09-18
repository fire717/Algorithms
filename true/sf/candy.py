#n个小孩一排 分糖果 最少糖果数  网上有的好像都没法ac
str1 = 'asdf'
str2 = 'asdd'

numbers = [3,1,0,2]
#numbers = numbers[::-1]
print('r',numbers)


def candy(numbers):
    l = len(numbers)
    nums = 1
    numbers[0]+=1
    t = 0
    add_tmp = [1]
    for i in range(1,l):
        nums+=1
        numbers[i]+=1
        add_tmp_t = 1
        if numbers[i]>numbers[i-1]-t:
            t+=1
            numbers[i]+=t
            nums+=t
            add_tmp_t+=t
        else:
            t = 0
        add_tmp.append(add_tmp_t)    
    #print(nums,numbers)
    #print(add_tmp)
    t = 0
    for j in range(2,l):
        #print(numbers[-j],numbers[-j+1],t)
        if numbers[-j]>numbers[-j+1]-t and numbers[-j]<numbers[-j-1]-t:
            t+=1
            t = max(add_tmp[-j],t+1)
            numbers[-j]+=t
            nums+=t
        else:
            t = 0
    if numbers[0]>numbers[1]:
        numbers[0]+=1
        nums+=1
    #print(nums,numbers)
    return nums


print(candy(numbers))
