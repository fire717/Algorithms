//Do this without extra space.
// c++ 果然没有python方便啊 好多方法都不知道怎么实现
class Solution {
public:
    bool isPalindrome(int x) {
        if(x<0 || (x!=0 &&x%10==0)) return false; // 小于0 和 个位为0直接排除
        int sum=0;
        while(x>sum) {
            sum = sum*10+x%10;
            x = x/10;
        }
        return (x==sum||(x==sum/10)); // 防止奇数位数
    }
};
