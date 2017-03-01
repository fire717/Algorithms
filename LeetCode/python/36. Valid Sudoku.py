# 开心，这个也完全是自己想出来的，76ms超过93%的人。代码思路很清晰，只是可能看着有点冗长，不知道还能否优化。

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(0,9):
            temp = []
            for j in range(0,9):
                if board[i][j]!='.' :
                    if board[i][j] not in temp:
                        temp.append(board[i][j])
                    else:
                        return False
        for i in range(0,9):
            temp = []
            for j in range(0,9):
                if board[j][i]!='.' :
                    if board[j][i] not in temp:
                        temp.append(board[j][i])
                    else:
                        return False
        for x in [0,3,6]:
            for y in [0,3,6]:
                temp = []
                for i in range(0,3):
                    for j in range(0,3):
                        if board[x+i][y+j]!='.' :
                            if board[x+i][y+j] not in temp:
                                temp.append(board[x+i][y+j])
                            else:
                                return False
        return True
