## 🧮 Python Calculator & Quadratic Solver
A simple command-line Python application that provides:
- Basic arithmetic operations on three numbers
- Quadratic equation solving using factorization logic
- This project is structured using object-oriented programming principles.

## 🚀 Features
1️⃣ Arithmetic Calculator
Performs operations on three numbers:
- Addition
- Subtraction
- Multiplication
- Division (with zero-division handling), Division safely handles ZeroDivisionError and returns an appropriate message 

2️⃣ Quadratic Equation Solver
Solves quadratic equations of the form:

    ax² + bx + c = 0

- Uses a factorization-based method
- Displays factor pairs if found
- Prints real roots when factorization succeeds
- Warns if a = 0
- Displays "no roots" if factorization fails 

⚠️ Note: This implementation works only when integer factorization is possible. It does not use the quadratic formula, so some valid quadratics may return "no roots" even if real roots exist.

## 🖥️ Menu System
After running:

1: simple math calculator
2: quadratic equation solver
3: exit

Choose the desired option and follow the prompts.

## 🧠 Concepts Used
- Object-Oriented Programming (Classes & Methods)
- Exception Handling (try-except)
- Loops and Conditional Statements
- Modular File Structure
- CLI-based User Interaction

## ⚠️ Limitations
- Quadratic solver only works when factorization is possible.
- No support for complex roots.
- Quadratic solver prints results instead of returning values.
- Coefficient a = 0 does not stop execution, only prints a warning.