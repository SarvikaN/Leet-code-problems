class Solution(object):
    def solveNQueens(self, n):
        res = []
        board = [["."] * n for _ in range(n)]
        def isSafe(r, c):
            for i in range(r):
                if board[i][c] == "Q":
                    return False
            i, j = r-1, c-1
            while i >= 0 and j >= 0:
                if board[i][j] == "Q":
                    return False
                i -= 1
                j -= 1
            i, j = r-1, c+1
            while i >= 0 and j < n:
                if board[i][j] == "Q":
                    return False
                i -= 1
                j += 1
            return True
        def backtrack(row):
            if row == n:
                temp = ["".join(r) for r in board]
                res.append(temp)
                return
            for col in range(n):
                if isSafe(row, col):
                    board[row][col] = "Q"
                    backtrack(row + 1)
                    board[row][col] = "."
        backtrack(0)
        return res
