# ATM Simulation
This project is a command-line ATM simulation built in Python using object-oriented programming principles. It allows users to create bank accounts, generate PINs, deposit and withdraw money, and manage balances with daily withdrawal limits. The system includes PIN-based authentication and persists account data using Python’s pickle module, ensuring information is saved between sessions. This project demonstrates practical implementation of OOP, file handling, and basic banking logic in a structured, real-world simulation.

## 📌 Features
- Account creation with auto-generated
- Secure PIN-based authentication
- Deposit functionality
- Withdrawal with:
    - Balance validation
    - Daily withdrawal limit control
- Account balance display
- Persistent storage using pickle
- Simple CLI-based menu interface

## 🛠 Technologies Used
- Python 3
- Object-Oriented Programming (OOP)
- File handling (pickle)
- Random PIN generation
- Basic security logic (PIN validation & daily limits)

## 📂 Project Structure
- ATM class handles account behavior:
    - deposit()
    - withdraw()
    - display()
- Account data stored in atm.pkl
- Menu-driven control system for user interaction

## 💾 Data Persistence
- All account data is saved locally using Python’s pickle module.
- Data automatically loads on startup and saves after transactions.

## 🚀 How It Works
- Open an account
- Generate or set a PIN
- Deposit an initial amount
- Access account using account number + PIN
- Perform deposits or withdrawals
- Data is automatically saved

## 🔐 Security Features
- PIN verification before transactions
- Structure for account locking after failed attempts
- Daily withdrawal limit enforcement

## 🎯 Purpose
- This project demonstrates:
    - OOP principles
    - State persistence
    - Input validation
    - Basic banking logic simulation