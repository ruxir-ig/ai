
def evaluate_employee():
    print("=== Employee Performance Evaluation Expert System ===")
    name = input("Enter Employee Name: ")

    score = 0
    print("\nRate each category:")
    perf = input("1️⃣ Work Performance (excellent/good/average/poor): ").lower()
    punct = input("2️⃣ Punctuality (always/usually/rarely): ").lower()
    team = input("3️⃣ Teamwork (team player/neutral/non-cooperative): ").lower()

    # Assign scores
    score_map = {
        "excellent": 3, "good": 2, "average": 1, "poor": 0,
        "always": 3, "usually": 2, "rarely": 1,
        "team player": 3, "neutral": 2, "non-cooperative": 1
    }

    score += score_map.get(perf, 0)
    score += score_map.get(punct, 0)
    score += score_map.get(team, 0)

    # Decision by range (not direct if-else logic)
    outcomes = {
        range(0, 4): "Needs Improvement ⚠️ (Training Required)",
        range(4, 7): "Satisfactory Employee 👍 (Keep it up)",
        range(7, 10): "Outstanding Employee ⭐ (Promotion Recommended)"
    }

    result = next(msg for r, msg in outcomes.items() if score in r)

    print(f"\n{name}'s Evaluation Result: {result}")
    print(f"Total Score: {score}/9")

if __name__ == "__main__":
    evaluate_employee()