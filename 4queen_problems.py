# Practical No. 4
def solve_n_queens(n):
    solutions = []
    
    def is_safe(board, row, col):
        for r in range(row):
            c = board[r]
            if c == col or abs(c - col) == abs(r - row):
                return False
        return True
    
    def place_queen(row, board):
        if row == n:
            solutions.append(board[:])
            return
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                place_queen(row + 1, board)
    
    board = [-1] * n
    place_queen(0, board)
    return solutions

result = solve_n_queens(4)
for sol in result:
    print(sol)