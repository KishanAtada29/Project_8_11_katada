# Subnet Planner 2.0

## Description

Subnet Planner is a Python command-line program that calculates subnet information from CIDR prefixes.

## Features

- Displays Class A, Class B and Class C subnet information
- Accepts CIDR values from /0 to /32
- Calculates subnet masks
- Calculates IPv4 address totals
- Valdiates user input
- Saves subnet reports to a JSON file
- Uses object-oriented programming with classes
- Includes automated unit tests
- Handles invalid user input with exception handling

## Project Files

- `main.py` controls the menu and progrma flow
- `cidr_input.py` handles CIDR input and displays results
- `cidr_desc.py` provides description for CIDR ranges 
- `classful_subnet_info.py` displays classful subnet information
- `functions.py` stores shared helper functions
- `subnetmask_calculator.py` converts CIDR prefix into subnet masks
- `subnet_report.py` stores and displays subnet report data
- `file_manager.py` saves subnet reports to JSON
- `saved_reports/subnet_report.json` stores saved report data
- `tests/test_subnet_calculator.py` contains automated unit tests

## How to Run

1. Open the project folder in VS Code.
2. Make sure Python is installed.
3. Run `main.py`.
4. Select an option from the menu.

## Video Presentation


Note: I recommend watching the presentation at 1.5x speed