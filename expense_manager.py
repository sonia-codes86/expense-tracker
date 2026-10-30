import json

from unicodedata import category



class Expense:
    def __init__(self,titel,amount,category,description):
        self.titel=titel
        self.amount=amount
        self.category=category
        self.description=description

    def __str__(self):
        return f"{self.titel} | {self.amount} | {self.category}"



class ExpenseManeger:
    def __init__(self):
        self.expenses=[]
        self.load_expenses()

    def load_expenses(self):
        self.expenses=[]
        try:
            with open("expenses.json","r",encoding='utf-8')as file:
                data = json.load(file)
                for item in data:
                    expense = Expense(item['titel'], item['amount'], item['category'], item['description'])
                    self.expenses.append(expense)

        except FileNotFoundError, json.JSONDecodeError:
            self.expenses = []


    def add_expense(self,titel,amount,category,description):
        expense=Expense(titel,amount,category,description)
        self.expenses.append(expense)
        with open("expenses.json", "w", encoding='utf-8') as file:
            json.dump([expense.__dict__ for expense in self.expenses], file, ensure_ascii=False, indent=4)

    def show_expense(self):
        result=[]
        for i,expense in enumerate(self.expenses,start=1):
            result.append (f"{i}- {expense.titel} | {expense.amount} | {expense.category}")
        return result

    def searech_expense(self,searech):
        for expense in self.expenses:
            if searech in expense.titel:
                return (f"خرید {expense.titel} | {expense.amount}")
        return ("can not find")

    def remove_expense(self,number_remove):
        if number_remove <= len(self.expenses) and number_remove > 0:
            self.expenses.pop(number_remove - 1)
            with open("expenses.json", "w", encoding='utf-8') as file:
                json.dump([expense.__dict__ for expense in self.expenses], file, ensure_ascii=False, indent=4)
            return ("removed successfully")
        else:
            return ("number not in list")

    def total_expense(self):
        total = 0
        for expense in self.expenses:
            total += expense.amount
        return (f"مجموع هزینه ها-->{total}تومان")

    def show_max_expense(self):
        if len(self.expenses) == 0:
            print("no expense")
            return
        max_item = max(self.expenses, key=lambda expense: expense.amount)
        return (f"بیشترین هزینه:{max_item.titel} - {max_item.amount}")











