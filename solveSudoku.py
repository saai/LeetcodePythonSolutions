class Solution:
	#check the value in i, j is valid
    def isValidSudoku(self, board,i,j):
        v = board[i][j]
        if v == '.':
            return True
        if int(v)>9:
            return False
        for n in xrange(9):
            c_hor = board[i][n]
            if c_hor == v and n != j:
                return False
            c_ver = board[n][j]
            if c_ver == v and n != i:
                return False
        for n in xrange(3):
            for m in xrange(3):
                i_hor = (i/3)*3+n
                j_ver = (j/3)*3+m
                c_temple = board[i_hor][j_ver]
                if c_temple == v and (i !=i_hor or j !=j_ver):
                    return False
        return True
                
    # @param {character[][]} board
    # @return {void} Do not return anything, modify board in-place instead.
    def solveSudoku(self, board):
        indexes = []
        for i in xrange(9):
            for j in xrange(9):
                if board[i][j] == '.':
                    index= i*9+j
                    indexes.append(index)
        l = len(indexes)
        p = 0
        while (p >= 0 and p < l):
            index = indexes[p]
            i = index/9
            j = index%9
            if board[i][j] == '.':
                # fill new 
                for q in range(1,10):
                    board[i][j] = str(q)
                    if self.isValidSudoku(board, i,j) == True:
                        break
                    else :
                        board[i][j] = '.'
                if board[i][j] == '.':
                    p-=1 # back trace
                else:
                    p+=1 # next
            else:
                if board[i][j]=='9':
                    board[i][j] = '.'
                    p -= 1
                    continue
                #else
                board[i][j] = str(int(board[i][j]) + 1)
                while(self.isValidSudoku(board,i,j)==False):
                    if board[i][j] == '9':
                        break
                    else:
                        board[i][j] = str(int(board[i][j])+1)
                if self.isValidSudoku(board, i, j):
                    p +=1 #next
                else:
                    board[i][j] = '.'
                    p -=1 # back trace
   