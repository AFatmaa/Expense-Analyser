import csv

def read_expenses(file_name):
  expenses = []

  with open(file_name, mode="r") as file:
    reader = csv.DictReader(file)

    for row in reader:
      expense = {
        "date": row["date"],
        "category": row["category"],
        "amount": float(row["amount"])
      }
      expenses.append(expense)
    
    return expenses
  
def calculate_total(expenses):
  total = 0

  for expense in expenses:
    total += expense["amount"]

  return total

def calculate_by_category(expenses):
  category_total = {}

  for expense in expenses:
    category = expense["category"]
    amount = expense["amount"]

    if category in category_total:
      category_total[category] += amount
    else:
      category_total[category] = amount
  
  return category_total

def get_top_category(category_totals):
  top_category = None
  top_amount = 0

  for category, amount in category_totals.items():
    if amount > top_amount:
      top_category = category
      top_amount = amount
    
  return {
    "category": top_category,
    "amount": top_amount,
  }

def main():
  expenses = read_expenses("expenses.csv")
  total = calculate_total(expenses)
  category_totals = calculate_by_category(expenses)
  top_category = get_top_category(category_totals)
  
  print(total)
  print(category_totals)
  print(top_category)

if __name__ == "__main__":
  main()