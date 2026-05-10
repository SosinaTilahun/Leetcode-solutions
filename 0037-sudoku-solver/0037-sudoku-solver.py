class Solution:
    def solveSudoku(self, board):
        rows = [[False] * 9 for _ in range(9)]
        cols = [[False] * 9 for _ in range(9)]
        boxes = [[False] * 9 for _ in range(9)]

        # initialize tracking tables
        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    num = ord(board[r][c]) - ord('1')
                    b = (r // 3) * 3 + (c // 3)
                    rows[r][num] = True
                    cols[c][num] = True
                    boxes[b][num] = True

        def backtrack(r, c):
            if r == 9:
                return True
            if c == 9:
                return backtrack(r + 1, 0)
            if board[r][c] != '.':
                return backtrack(r, c + 1)

            b = (r // 3) * 3 + (c // 3)

            for num in range(9):
                if not rows[r][num] and not cols[c][num] and not boxes[b][num]:
                    board[r][c] = chr(num + ord('1'))
                    rows[r][num] = cols[c][num] = boxes[b][num] = True

                    if backtrack(r, c + 1):
                        return True

                    # undo
                    board[r][c] = '.'
                    rows[r][num] = cols[c][num] = boxes[b][num] = False

            return False

        backtrack(0, 0)