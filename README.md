# Expense Tracker

A simple Python program that simulates an expense tracking system using an in-memory data structure. It records expenses, validates input, and calculates totals overall and by category.

## Overview

This project simulates a basic personal expense tracker without a real database. It uses a single Python list to act as in-memory storage:

- `expenses` — stores all expense entries, each as a dictionary with `amount`, `category`, and `description`

The system validates each expense before adding it, and provides functions to summarize spending.

## Features

- **Expense validation** — rejects any amount that is not greater than 0
- **Add expenses** — stores each expense as a structured dictionary
- **Total calculation** — sums the amount across all recorded expenses
- **Category totals** — sums the amount for a single specified category
- **Readable expense listing** — displays all stored expenses in a clear format
- **Built-in test cases** — demonstrates both valid and invalid expense entries

## How It Works

1. `add_expense(amount, category, description)` validates that `amount` is greater than 0, raising a `ValueError` if not. On success, it builds an expense dictionary and appends it to `expenses`, then returns it.
2. `calculate_total_expenses()` loops through `expenses` and returns the sum of all amounts.
3. `calculate_total_by_category(category)` loops through `expenses` and returns the sum of amounts matching the given category.
4. `show_expenses()` prints every expense in `expenses` in a clear, readable format.

## Project Structure

```
├── expense_tracker.py   # Main script: data storage, functions, and tests
└── README.md
```

## Requirements

- Python 3.x
- No external dependencies (standard library only)

## Usage

Run the script directly to see the expense tracker in action:

```bash
python expense-tracker.py
```

The script includes a testing section at the bottom that:

| Step | Action                                   |
|------|--------------------------------------------|
| 1    | Adds multiple valid expenses                |
| 2    | Attempts to add at least one invalid expense (amount ≤ 0) |
| 3    | Prints the total of all expenses            |
| 4    | Prints the total for a specific category    |
| 5    | Displays all stored expenses                |

## Example Output

```
Added expense: {'amount': 50, 'category': 'Food', 'description': 'Groceries'}
Added expense: {'amount': 20, 'category': 'Transport', 'description': 'Bus ticket'}
Failed to add expense: Amount must be greater than 0.

Total expenses: 70
Total for 'Food': 50

All Expenses:
- Food: 50 (Groceries)
- Transport: 20 (Bus ticket)
```

## Validation Rules Summary

| Field | Rule                        |
|-------|------------------------------|
| amount | Must be greater than 0       |

## Author

Ahmed Reda
