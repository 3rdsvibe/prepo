"""Drop"""

def main():
    """Drop"""
    grade = float(input())
    if grade < 1.00:
        print("I'm so sad.")
    elif grade < 2.00:
        ans = 4.00 - grade
        print("%.2f"%(ans))
    elif grade >= 2.00:
        print("I'm so happy.")

main()
