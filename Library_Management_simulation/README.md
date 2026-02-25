# 📚 Library Management System (Python)
- A command-line based Library Management System built using Python.
- This project simulates core library operations such as adding books, registering borrowers,borrowing/returning books, and persistent data storage using pickle.

## 🚀 Features
- Add and remove books
- Register borrowers
- Borrow and return books
- Prevent borrowing of already borrowed books
- Prevent deletion of borrowed books
- Persistent data storage using pickle
- Simple CLI-based interactive menu

## 🧱 Project Structure
- Book class – Represents a book with status tracking
- Borrower class – Represents a borrower with borrowed book history
- File persistence using library.pkl

## 💾 Data Persistence
- All data is stored locally in a library.pkl file using Python's built-in pickle module.
- The system automatically loads existing data at startup and saves changes after every operation.

## 🛠️ Technologies Used
- Python 3
- Pickle (for serialization)

## ▶️ How to Run

Run:
python library.py

## 📌 Learning Highlights
- Object-Oriented Programming (OOP)
- File Handling & Serialization
- Dictionary-based data management
- Basic input validation
- State management in CLI applications