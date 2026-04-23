
from collections import Counter

def analyze_expenses(data):
    total = sum(item["amount"] for item in data)

    categories = [item["category"] for item in data]
    freq = Counter(categories)

    # Detect frequent habits (more than 2 times)
    frequent = {k: v for k, v in freq.items() if v >= 2}

    return {
        "total_spent": total,
        "category_frequency": dict(freq),
        "frequent_habits": frequent
    }