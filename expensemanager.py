import os
import pickle
from expense import Expense

DATA_FILE = "expenses.pkl"


class ExpenseManager:
    def __init__(self, filename=DATA_FILE):
        self.filename = filename
        self.expenses = []
        self.load()

    # ---------- persistence (pickle) ----------
    def save(self):
        """Write expenses to disk. Uses a temp file so a crash can't corrupt the data."""
        tmp_name = self.filename + ".tmp"
        with open(tmp_name, "wb") as f:
            pickle.dump(self.expenses, f)
        os.replace(tmp_name, self.filename)

    def load(self):
        """Load expenses from disk. Starts empty if file is missing or unreadable."""
        if not os.path.exists(self.filename):
            self.expenses = []
            return
        try:
            with open(self.filename, "rb") as f:
                self.expenses = pickle.load(f)
        except (pickle.UnpicklingError, EOFError, AttributeError, ImportError):
            print("Warning: saved data could not be read. Starting with an empty list.")
            self.expenses = []

    # ---------- expense operations ----------
    def add_expense(self, amount, category, description, date):
        self.expenses.append(Expense(amount, category, description, date))
        self.save()

    def view_expenses(self):
        return self.expenses

    def search_expenses(self, category=None, start_date=None, end_date=None):
        results = self.expenses

        if category:
            results = [e for e in results if e.category.lower() == category.lower()]
        if start_date:
            results = [e for e in results if e.date >= start_date]
        if end_date:
            results = [e for e in results if e.date <= end_date]

        return results

    def delete_expense(self, index):
        if 0 <= index < len(self.expenses):
            del self.expenses[index]
            self.save()
            return True
        return False