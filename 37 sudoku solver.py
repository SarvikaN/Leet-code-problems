class Solution(object):
    def solveSudoku(self, board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    num = board[i][j]
                    rows[i].add(num)
                    cols[j].add(num)
                    boxes[(i//3)*3 + j//3].add(num)
        def backtrack(i, j):
            if i == 9:
                return True
            if j == 9:
                return backtrack(i + 1, 0)
            if board[i][j] != ".":
                return backtrack(i, j + 1)
            for ch in "123456789":
                box_id = (i//3)*3 + j//3
                if ch not in rows[i] and ch not in cols[j] and ch not in boxes[box_id]:
                    board[i][j] = ch
                    rows[i].add(ch)
                    cols[j].add(ch)
                    boxes[box_id].add(ch)
                    if backtrack(i, j + 1):
                        return True
                    board[i][j] = "."
                    rows[i].remove(ch)
                    cols[j].remove(ch)
                    boxes[box_id].remove(ch)
            return False
        backtrack(0, 0)
