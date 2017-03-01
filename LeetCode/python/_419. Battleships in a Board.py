# NO TIME!
'''
由于board中的战舰之间确保有'.'隔开，因此遍历board，若某单元格为'X'，只需判断其左边和上边的相邻单元格是否也是'X'。
如果左邻居或者上邻居单元格是'X'，则说明当前单元格是左边或者上边战舰的一部分；
否则，令计数器+1
'''

class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        h = len(board)
        w = len(board[0]) if h else 0

        ans = 0
        for x in range(h):
            for y in range(w):
                if board[x][y] == 'X':
                    if x > 0 and board[x - 1][y] == 'X':
                        continue
                    if y > 0 and board[x][y - 1] == 'X':
                        continue
                    ans += 1
        return ans
