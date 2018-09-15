from bisect import bisect_left
#查找该数值将会插入的位置并返回，而不会插入。

def long_increasing_subsequence(x):
    n = len(x)
    p = [None]*n
    h = [None]
    b = [float('-inf')]
    for i in range(n):
        if x[i]>b[-1]:
            p[i] = h[-1]
            h.append(i)
            b.append(x[i])
        else:
            # 二分查找 b[k-1] < x[i] <=b[k]
            k = bisect_left(b,x[i])
            h[k] = i
            b[k] = x[i]
            p[i] = h[k-1]
        print(p,h,b)
    q = h[-1]
    s = []
    while q is not None:
        s.append(x[q])
        q = p[q]
    return s[::-1]

x = [2,1,3,2,4]
print(long_increasing_subsequence(x))
