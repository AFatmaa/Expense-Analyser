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

def main():
  expenses = read_expenses("expenses.csv")
  print(expenses)

if __name__ == "__main__":
  main()