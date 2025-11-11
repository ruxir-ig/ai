# Practical No. 3 - Alpha-Beta Tree Search

def alpha_beta(nums, depth, alpha, beta, is_max):
    if depth == 0 or len(nums) == 1:
        return nums[0]
    if is_max:
        best = -9999
        for new_nums in get_moves(nums):
            val = alpha_beta(new_nums, depth - 1, alpha, beta, False)
            best = max(best, val)
            alpha = max(alpha, val)
            if beta <= alpha:
                break
        return best
    else:
        best = 9999
        for new_nums in get_moves(nums):
            val = alpha_beta(new_nums, depth - 1, alpha, beta, True)
            best = min(best, val)
            beta = min(beta, val)
            if beta <= alpha:
                break
        return best

def get_moves(nums):
    moves = []
    if len(nums) > 1:
        moves.append(nums[1:])
        moves.append(nums[:-1])
    return moves

nums = list(map(int, input("Enter numbers separated by space: ").split()))
depth = len(nums) - 1
print("\nNumbers:", nums)
print("Best score (Alpha-Beta Search):", alpha_beta(nums, depth, -9999, 9999, True))
