# Basic Calculator

A simple Python calculator module that provides basic arithmetic operations following Python's style guidelines (PEP 8) and proper documentation (PEP 257).

## Features

- Addition
- Subtraction
- Multiplication
- Division
- Modulo operation
- Type hints for better code readability
- Proper error handling for division by zero
- Comprehensive docstrings

## Requirements

- Python 3.6 or higher

## Usage

### As a Command Line Tool

Run the calculator from the command line:

```
python calculator.py
```

You will be prompted to enter two numbers, and the program will display the results of all basic arithmetic operations.

### As a Module in Your Code

```python
from calculator import Calculator

# Create a calculator instance
calc = Calculator(10, 5)

# Perform operations using instance values
addition = calc.add()          # 15
subtraction = calc.sub()       # 5
multiplication = calc.mul()    # 50
division = calc.div()          # 2.0
modulo = calc.mod()            # 0

# Or perform operations with custom values
custom_addition = calc.add(20, 30)  # 50
```

## Error Handling

The calculator handles common errors:

- ValueError: When non-numeric inputs are provided
- ZeroDivisionError: When attempting to divide by zero

## Structure

The code follows Python best practices:
- Properly typed parameters and return values
- Comprehensive docstrings describing functionality
- Clean code organization following PEP 8 style guidelines 