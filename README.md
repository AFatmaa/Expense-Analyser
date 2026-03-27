# Expense Analyser

A simple Python project that reads expense data from a CSV file and generates a spending report.

## Features

- Read expense data from a CSV file
- Calculate total spending
- Group spending by category
- Identify the top spending category
- Display a formatted report in the terminal
- Handle missing file errors gracefully

## Technologies

- Python
- csv module

## Project Structure

```
expense-analyser/
├── main.py
├── expenses.csv
└── README.md
```

## Example CSV Format

```csv
date,category,amount
2026-03-01,food,20.50
2026-03-02,transport,15.00
2026-03-03,food,30.00
2026-03-04,shopping,50.00
2026-03-05,bills,80.00
```

## How to Run

1. Make sure Python is installed
2. Open the project folder in VS Code
3. Run the following command in the terminal:
      ```bash
      python3 main.py
      ```

## Example Output

```
Expense Report
------------------------------
Total spending: £195.50

Spending by category:
- food: £50.50
- transport: £15.00
- shopping: £50.00
- bills: £80.00

Top category:
bills: £80.00
```