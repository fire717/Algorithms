# 3 ms -24%
# c++中可直接对十进制数字进行位运算
class Solution {
public:
    int hammingDistance(int x, int y) {
       int z=x^y;
        //^符号表示：按位异或运算符。
       int count=0;
       while(z != 0 ) {
         if (z&1)count++;
         z>>=1;
       }  
       return count; 
    }
};
