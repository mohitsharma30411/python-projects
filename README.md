# Python Practice Projects

A collection of beginner-level Python projects created to practice and strengthen core Python programming concepts through small real-world applications.

## Projects

This repository currently contains three projects:

1. 🧰 Hardware Shop Bill Generator
2. ⚡ Electricity Billing System
3. 🏧 ATM Simulator

---

# 1. 🧰 Hardware Shop Bill Generator

## Description

A simple hardware shop billing program that allows a customer to select multiple hardware products, enter quantities, and generate a formatted invoice.

## Features

* Predefined hardware product list with prices
* Display available products
* Accept product name and quantity
* Calculate individual product amount
* Support multiple products in a single bill
* Calculate total bill amount
* Generate a formatted invoice

## Sample Products

```text
Hammer      ₹450
Screwdriver ₹180
Tape        ₹250
Drill       ₹3200
Pipe        ₹520
Tap         ₹650
Wrench      ₹650
Pliers      ₹380
Wire        ₹1800
```

## Python Concepts Used

* Functions
* Dictionaries
* Lists
* List of dictionaries
* `while` loop
* `for` loop
* `if-else`
* `break`
* `continue`
* User input
* Type conversion
* Arithmetic operations
* f-strings
* Formatted output

## Example

```text
==================================================
                 HARDWARE STORE
==================================================
Product                  Qty     Price     Amount
--------------------------------------------------
Hammer                   2       450       900
Tape                     3       250       750
Nail                     2       140       280
--------------------------------------------------
Total                                     1930
==================================================
```

---

# 2. ⚡ Electricity Billing System

## Description

A simple electricity billing system that calculates the electricity bill based on the number of units consumed using a slab-based billing structure.

The program also accepts customer information and displays the calculated bill.

## Billing Slabs

| Units         |      Rate |
| ------------- | --------: |
| 0–99          |   ₹2/unit |
| 100–199       | ₹3.5/unit |
| 200–249       | ₹4.5/unit |
| 250–299       |   ₹6/unit |
| 300 and above |   ₹8/unit |

## Features

* Accept customer name
* Accept customer ID
* Accept meter number
* Accept previous meter reading
* Accept current meter reading
* Calculate consumed units
* Validate meter readings
* Calculate charges according to slabs
* Display slab-wise units and amount
* Display total electricity bill

## Calculation

```text
Units Consumed = Current Meter Reading - Previous Meter Reading
```

The program then divides the consumed units across the applicable billing slabs and calculates the corresponding amount.

## Python Concepts Used

* Functions
* `if-elif-else` / conditional logic
* `while` loop
* `for` loop
* Lists
* List of tuples
* Dictionaries
* User input
* Type conversion
* Arithmetic operations
* `sum()`
* String formatting
* f-strings
* Input validation

## Example

```text
**************************************************
           Electricity Slab System
**************************************************
0-99                     2/unit
100-199                  3.5/unit
200-249                  4.5/unit
250-299                  6/unit
300 above                8/unit
```

---

# 3. 🏧 ATM Simulator

## Description

A basic ATM simulation program that demonstrates PIN validation, account balance checking, withdrawal, PIN change, and transaction control.

## Features

* Set a 6-digit ATM PIN
* Validate PIN format
* Allow up to 3 PIN verification attempts
* Display account balance
* Withdraw money
* Check available balance before withdrawal
* Change ATM PIN
* Exit the ATM session
* Display meaningful transaction messages

## ATM Menu

```text
1. Balance Check
2. Withdraw
3. PIN Change
4. Exit
```

## PIN Validation

The program validates that the PIN:

* Contains exactly 6 digits
* Contains numeric characters only

During transaction verification, the customer receives up to three attempts to enter the correct PIN.

## Withdrawal

Before processing a withdrawal, the program checks whether the requested amount is available in the account balance.

Example:

```text
Available Balance : 10000

Enter amount to Withdraw: 3000

Withdraw is successful
Please collect your money
Remaining Balance: 7000
```

## Python Concepts Used

* Functions
* `while` loop
* `for` loop
* `if-elif-else`
* `break`
* `return`
* `for-else`
* String methods
* `len()`
* `isdigit()`
* User input
* Type conversion
* Arithmetic operations
* Input validation

---

# Python Skills Practiced

These three projects provide practice with the following Python concepts:

```text
                    Python Fundamentals
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
    Functions           Loops             Conditions
        │                  │                  │
        ├──────────────┬───┴──────────────┐   │
        │              │                  │   │
    Dictionaries      Lists          Input Validation
        │              │                  │
        └──────────────┼──────────────────┘
                       │
                 Data Processing
                       │
                Calculations
                       │
                Formatted Output
```

---

# Learning Progression

The projects were developed to practice Python progressively:

```text
Basic Input
     ↓
Variables & Data Types
     ↓
Conditions
     ↓
Loops
     ↓
Functions
     ↓
Lists & Dictionaries
     ↓
Input Validation
     ↓
Calculations
     ↓
Formatted Output
     ↓
Real-world Mini Projects
```

---

# Future Improvements

These projects can be extended as my Python skills improve.

## Hardware Shop Billing

Possible future improvements:

* Product validation
* Quantity validation
* Discount calculation
* GST calculation
* Customer details
* Bill number generation
* Save bills to files
* Excel integration using `openpyxl`

## Electricity Billing

Possible future improvements:

* Better input validation
* Fixed charges
* Additional taxes
* Due date calculation
* Previous bill history
* Save bills to files
* Excel integration
* Monthly consumption reports

## ATM Simulator

Possible future improvements:

* Multiple customer accounts
* Account numbers
* Transaction history
* Daily withdrawal limit
* Withdrawal denomination validation
* File-based account storage
* Exception handling
* Secure password/PIN handling

---

# Technologies Used

```text
Python 3
```

Future versions may include:

```text
Python
openpyxl
CSV
SQLite
pandas
```

---

# Repository Structure

```text
python-projects/
│
├── hardware-shop-billing/
│   ├── hardware_bill.py
│   └── README.md
│
├── electricity-billing/
│   ├── electricity_bill.py
│   └── README.md
│
├── atm-simulator/
│   ├── atm.py
│   └── README.md
│
└── README.md
```

---

# About

These projects are part of my Python learning journey and are focused on building programming fundamentals through practical, real-world examples.

The projects will be progressively improved as I learn additional Python concepts such as file handling, exception handling, Excel automation, databases, and data analysis.

---

## Current Learning Focus

```text
Python Fundamentals
        ↓
File Handling
        ↓
Excel Automation
        ↓
SQL
        ↓
Pandas
        ↓
Data Analysis
```
