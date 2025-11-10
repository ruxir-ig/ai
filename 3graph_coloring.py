# Practical No. 3 - Alpha-Beta Tree Search

# Global counter to track pruning efficiency
nodes_explored = 0
nodes_pruned = 0


def minimax_alpha_beta(depth, node_index, is_maximizing, scores, height, alpha, beta):
    """
    Alpha-Beta Pruning Algorithm for a simple game tree

    Args:
        depth: Current depth in tree
        node_index: Index of current node
        is_maximizing: True if maximizer's turn
        scores: List of leaf node scores
        height: Maximum height of tree
        alpha: Best value for maximizer
        beta: Best value for minimizer
    """
    global nodes_explored, nodes_pruned

    # Terminal node (leaf)
    if depth == height:
        nodes_explored += 1
        return scores[node_index]

    if is_maximizing:
        max_score = float("-inf")

        # Explore two children
        for i in range(2):
            child_index = node_index * 2 + i
            score = minimax_alpha_beta(
                depth + 1, child_index, False, scores, height, alpha, beta
            )
            max_score = max(max_score, score)
            alpha = max(alpha, score)

            # Alpha-Beta Pruning
            if beta <= alpha:
                nodes_pruned += 1
                print(f"  [PRUNED] at depth {depth}, node {node_index}, child {i}")
                print(f"           Beta ({beta}) <= Alpha ({alpha})")
                break

        return max_score

    else:
        min_score = float("inf")

        # Explore two children
        for i in range(2):
            child_index = node_index * 2 + i
            score = minimax_alpha_beta(
                depth + 1, child_index, True, scores, height, alpha, beta
            )
            min_score = min(min_score, score)
            beta = min(beta, score)

            # Alpha-Beta Pruning
            if beta <= alpha:
                nodes_pruned += 1
                print(f"  [PRUNED] at depth {depth}, node {node_index}, child {i}")
                print(f"           Beta ({beta}) <= Alpha ({alpha})")
                break

        return min_score


def demonstrate_alpha_beta():
    """Demonstrate Alpha-Beta pruning on a game tree"""
    global nodes_explored, nodes_pruned

    print("=" * 60)
    print("Alpha-Beta Tree Search Demonstration")
    print("=" * 60)
    print("\nGame Tree Structure:")
    print("                 Root")
    print("              /        \\")
    print("           MAX          MAX")
    print("          /   \\        /   \\")
    print("        MIN   MIN    MIN   MIN")
    print("        / \\   / \\    / \\   / \\")
    print("Leaves: 3 5  2 9   12 8  14 6")
    print()

    # Leaf node scores (8 leaves in a binary tree of height 3)
    scores = [3, 5, 2, 9, 12, 8, 14, 6]
    height = 3  # Tree height

    print("Leaf scores:", scores)
    print("\nStarting Alpha-Beta Search...")
    print("-" * 60)

    nodes_explored = 0
    nodes_pruned = 0

    optimal_value = minimax_alpha_beta(
        0, 0, True, scores, height, float("-inf"), float("inf")
    )

    print("-" * 60)
    print(f"\nOptimal value: {optimal_value}")
    print(f"Nodes explored: {nodes_explored}")
    print(f"Branches pruned: {nodes_pruned}")
    print(f"Total possible leaf nodes: {len(scores)}")
    print(f"Efficiency: Avoided exploring {len(scores) - nodes_explored} nodes")
    print("\nExplanation:")
    print("- MAX player tries to maximize the score")
    print("- MIN player tries to minimize the score")
    print("- Alpha-Beta pruning skips branches that won't affect final decision")
    print("=" * 60)


def interactive_mode():
    """Let user define their own tree"""
    print("\n\nInteractive Mode - Define Your Own Tree")
    print("-" * 60)

    try:
        num_leaves = int(input("Enter number of leaf nodes (power of 2, e.g., 4, 8): "))
        if num_leaves & (num_leaves - 1) != 0:
            print("Must be power of 2! Using 8.")
            num_leaves = 8

        print(f"Enter {num_leaves} leaf scores (space-separated):")
        scores = list(map(int, input().split()))

        if len(scores) != num_leaves:
            print(f"Expected {num_leaves} scores, using default.")
            scores = [3, 5, 2, 9, 12, 8, 14, 6]

        import math

        height = int(math.log2(num_leaves))

        global nodes_explored, nodes_pruned
        nodes_explored = 0
        nodes_pruned = 0

        print(f"\nYour leaf scores: {scores}")
        print("Searching...\n")

        optimal_value = minimax_alpha_beta(
            0, 0, True, scores, height, float("-inf"), float("inf")
        )

        print(f"\nOptimal value: {optimal_value}")
        print(f"Nodes explored: {nodes_explored}")
        print(f"Branches pruned: {nodes_pruned}")
        
    except:
        print("Invalid input, skipping interactive mode.")


if __name__ == "__main__":
    # Demonstrate with predefined tree
    demonstrate_alpha_beta()

    # Interactive mode
    choice = input("\nTry interactive mode? (y/n): ")
    if choice.lower() == "y":
        interactive_mode()
