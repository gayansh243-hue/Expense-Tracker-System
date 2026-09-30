def show_summary(expenses):
    """Total spent per category, as a dict."""
    summary = {}
    for expense in expenses:
        summary[expense.category] = summary.get(expense.category, 0) + expense.amount
    return summary


def show_overall_summary(expenses):
    """Returns (total, average). Average is 0 when there are no expenses."""
    total = sum(e.amount for e in expenses)
    average = total / len(expenses) if expenses else 0
    return total, average


def show_category_summary(expenses, category):
    return sum(e.amount for e in expenses
               if e.category.lower() == category.lower())