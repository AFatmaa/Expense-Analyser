import csv

def read_expenses(file_name):
  expenses = []

  try:
    with open(file_name, mode="r") as file:
      reader = csv.DictReader(file)

      for row in reader:
        expense = {
          "date": row["date"],
          "category": row["category"],
          "amount": float(row["amount"])
        }
        expenses.append(expense)

  except FileNotFoundError:
    print(f"Error: The file '{file_name}' was not found.")
    return []
    
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

def print_report(total, average, category_totals, top_category):
  print("\nExpense Report")
  print("-" * 30)
  print(f"Total spending: £{total:.2f}\n")
  print(f"Average expense: £{average:.2f}\n")

  print("Spending by category:")
  for category, amount in category_totals.items():
    print(f"- {category}: £{amount:.2f}")
  
  print("\nTop category:")
  print(f"{top_category['category']}: £{top_category['amount']:.2f}")

def calculate_average(expenses):

  if not expenses:
      return 0
  
  total = calculate_total(expenses)
  average = total / len(expenses)

  return average

def main():
  file_name = "expenses.csv"
  expenses = read_expenses(file_name)

  if not expenses:
    return
  
  total = calculate_total(expenses)
  average = calculate_average(expenses)
  category_totals = calculate_by_category(expenses)
  top_category = get_top_category(category_totals)
  
  print_report(total, average, category_totals, top_category)

if __name__ == "__main__":
  main()