# Expense Tracker Management System

## Project Description

The **Expense Tracker Management System** is a simple Python console application used to record, view, search, delete, and analyze personal expenses.

The project is designed using Python modules and basic Object-Oriented Programming concepts.

## Features

- Add a new expense
- View all expenses
- Search expenses by category
- Delete an expense
- Display total and average spending
- Display spending by category
- Simple menu-driven interface

## Project Structure

```text
Expense_Tracker_Management_System/
│
├── main.py
├── expense.py
├── expense_manager.py
├── reports.py
└── README.md
```

### Module Description

**1. main.py**
- Contains the main menu.
- Takes input from the user.
- Connects all other modules.

**2. expense.py**
- Contains the `Expense` class.
- Stores amount, category, description, and date.

**3. expense_manager.py**
- Manages the list of expenses.
- Adds, displays, searches, and deletes expenses.

**4. reports.py**
- Calculates total and average expenses.
- Generates a category-wise expense report.

## Requirements

- Python 3.x
- No external libraries are required.

## How to Run

1. Download or clone this repository.
2. Open the project folder in VS Code or a terminal.
3. Run:

```bash
python main.py
```

## Example

```text
========== EXPENSE TRACKER MANAGEMENT SYSTEM ==========
1. Add Expense
2. View All Expenses
3. Search Expenses by Category
4. Delete Expense
5. Show Expense Summary
6. Show Category Report
7. Exit
```

## Data Storage

This basic version stores expenses in a Python list and dictionary structure while the program is running.

**Note:** Data is not permanently stored after the program is closed.

## Concepts Used

- Python classes and objects
- Lists
- Dictionaries
- Functions
- Modules
- Loops
- Conditional statements
- Exception handling
- String formatting

## Author

Student Project - Python
