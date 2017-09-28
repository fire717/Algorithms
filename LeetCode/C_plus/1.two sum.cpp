//可喜可贺 第一道C++的题 ：）...
//162 ms-26%    暴力法居然还有26 ...
/*
向量 vector 是一种对象实体, 能够容纳许多其他类型相同的元素, 因此又被称为容器。 
与string相同, vector 同属于STL(Standard Template Library, 标准模板库)中的一种自定义的数据类型, 可以广义上认为是数组的增强版。
在使用它时, 需要包含头文件 vector, #include<vector>

感觉就类似于python中的list嘛。
这篇博客写的不错：
http://www.cnblogs.com/mr-wid/archive/2013/01/22/2871105.html
*/

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> ans(2,0);
        int l;    
        l = nums.size();
        for(int i=0;i<l-1;i++){
            for(int j=i+1;j<l;j++){
                if( nums[i] + nums[j] == target ){
                    ans[0] = i;
                    ans[1] = j;
                }
            }
        }
        return ans;
    }
};
