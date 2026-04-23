# main.py

from storage import add_expense, load_data
from analysis import analyze_expenses
from ai import generate_ai_response


def get_user_input():
    print("\nEnter your expense")

    category = input("Category (food/pathao/icecream/misc): ").strip().lower()

    try:
        amount = float(input("Amount: "))
    except ValueError:
        print("Invalid amount. Try again.")
        return None

    return {
        "category": category,
        "amount": amount
    }


def ask_user_questions():
    print("\nAnswer a couple of questions (optional, press enter to skip)")

    q1 = input("Q1: ")
    q2 = input("Q2: ")

    return {"q1": q1, "q2": q2}


def display_analysis(report):
    print("\nSpending Overview")

    print(f"Total spent: Rs {report['total_spent']}")

    print("\nCategory usage:")
    for category, count in report["category_frequency"].items():
        print(f"  {category}: {count} times")

    if report["frequent_habits"]:
        print("\nHabits you repeat often:")
        for k, v in report["frequent_habits"].items():
            print(f"  {k}: {v} times")


def display_ai_output(ai_output):
    print("\nYour AI Finance Assistant says:\n")
    print(ai_output)


if __name__ == "__main__":
    expense = get_user_input()

    if expense:
        add_expense(expense)

        data = load_data()
        report = analyze_expenses(data)

        display_analysis(report)

        ai_output = generate_ai_response(data, report)
        display_ai_output(ai_output)

        ask_user_questions()

        print("\nSaved. See you tomorrow.")