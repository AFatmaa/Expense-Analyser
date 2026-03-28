import csv
DEFAULT_FILE_NAME = "expenses.csv"
REPORT_LINE_LENGTH = 30

def read_expenses(file_name):
  """Read expenses from a CSV file and return a list of dictionaries."""
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
  """Calculate the total amount from all expenses."""
  total = 0

  for expense in expenses:
    total += expense["amount"]

  return total

def calculate_by_category(expenses):
  """Group expenses by category and calculate total spending for each category."""
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
  """Return the category with the highest total spending."""
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

def calculate_average(expenses):
  """Calculate the average amount per expense."""
  if not expenses:
      return 0
  
  total = calculate_total(expenses)
  average = total / len(expenses)

  return average

def calculate_category_averages(expenses):
  """Calculate the average expense amount for each category."""
  category_data = {}

  for expense in expenses:
    category = expense["category"]
    amount = expense["amount"]

    if category not in category_data:
      category_data[category] = {"total": 0, "count": 0}

    category_data[category]["total"] += amount
    category_data[category]["count"] += 1
  
  category_averages = {}

  for category, data in category_data.items():
    avg = data["total"] / data["count"]
    category_averages[category] = avg

  return category_averages

def get_highest_expense(expenses):
  """Return the single highest expense entry."""
  highest_expense = expenses[0]

  for expense in expenses:
    if expense["amount"] > highest_expense["amount"]:
      highest_expense = expense

  return highest_expense

def print_report(
    total, 
    average, 
    category_totals, 
    category_averages, 
    top_category,
    highest_expense,
):
  """Print a formatted expense report to the terminal."""
  print("\nExpense Report")
  print("-" * REPORT_LINE_LENGTH)
  print(f"Total spending: £{total:.2f}\n")
  print(f"Average expense: £{average:.2f}\n")

  print("Spending by category:")
  sorted_category_totals = sorted(
    category_totals.items(),
    key=lambda item: item[1],
    reverse=True,
  )

  for category, amount in sorted_category_totals:
    print(f"- {category}: £{amount:.2f}")

  print(f"\nAverage by category:")
  sorted_category_averages = sorted(
    category_averages.items(),
    key=lambda item: item[1],
    reverse=True,
  )

  for category, avg in sorted_category_averages:
    print(f"- {category}: £{avg:.2f}")
  
  print("\nTop category:")
  print(f"{top_category['category']}: £{top_category['amount']:.2f}")

  print("\nHighest single expense")
  print(
    f"- {highest_expense['category']} on {highest_expense['date']}: "
    f"£{highest_expense['amount']:.2f}"
  )

def main():
  """Run the expense analyser application."""
  file_name = input(f"Enter CSV file name (default: {DEFAULT_FILE_NAME}): ").strip() or DEFAULT_FILE_NAME
  
  expenses = read_expenses(file_name)

  if not expenses:
    return
  
  total = calculate_total(expenses)
  average = calculate_average(expenses)
  category_totals = calculate_by_category(expenses)
  category_averages = calculate_category_averages(expenses)
  top_category = get_top_category(category_totals)
  highest_expense = get_highest_expense(expenses)
  
  print_report(
    total, 
    average, 
    category_totals, 
    category_averages, 
    top_category,
    highest_expense,
  )

if __name__ == "__main__":
  main()