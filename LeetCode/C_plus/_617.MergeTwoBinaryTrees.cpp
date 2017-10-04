//不熟悉c++中的树结构（类值的引用）
//c++中当定义类对象是指针对象时候，就需要用到->指向类中的成员；
//当定义一般对象时候时就需要用到"."指向类中的成员。
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* mergeTrees(TreeNode* t1, TreeNode* t2) {
        if ( t1 && t2 ) {
            TreeNode* root = new TreeNode(t1->val + t2->val); 
            //声明新对象要加new
            root->left = mergeTrees(t1->left, t2->left);
            root->right = mergeTrees(t1->right, t2->right);
            return root;
        } else {
            return t1 ? t1 : t2;
        }
    }
};
