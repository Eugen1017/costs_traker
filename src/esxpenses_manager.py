import datetime
import json
import os

class Expanse:
    def __init__(self, date, amount, category, description):
        self.date = date
        self.amount = amount
        self.category = category
        self.description = description


class ExpenseManager:
    def __init__(self):
        self.expenses = []
        self.file_path = os.path.join(os.path.dirname(__file__), '..', 'expenses.json')

    def add_expense(self, date, amount, category, description):
        self.expenses.append(Expanse(date, amount, category, description))

    def remove_expense(self, expense: Expanse) -> None:
        self.expenses.remove(expense)

    def load_from_file(self) -> None:
        with open(self.file_path, 'r', encoding='utf-8') as json_file:
            try:
                data = json.load(json_file)
            except json.decoder.JSONDecodeError:
                data = {}

        for expense in data:
            self.expenses.append(Expanse(
                expense["date"], expense["amount"],
                expense["category"], expense["description"])
            )

    def load_to_file(self) -> None:
        data_to_write = [exp.__dict__ for exp in self.expenses]

        with open(self.file_path, 'w') as json_file:
            json.dump(data_to_write, json_file)

    def show(self):
        print([exp.__dict__ for exp in self.expenses])


test_expense = ExpenseManager()

test_expense.load_from_file()

test_expense.show()

test_expense.add_expense("2025-06-27", 50, "coffee", "mall")
test_expense.show()
test_expense.load_to_file()