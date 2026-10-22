# Global Digital Bank - Core Account Engine

A robust, enterprise-grade Core Banking Account Management System built in **Java** and **Python**.

This project demonstrates the progressive evolution of backend domain logic, moving from basic Object-Oriented Models to defensive programming, security rules, and custom exception-driven architecture.

---

## 🌟 Key Features

- **Account Management**: Support for `Savings` and `Current` account types.
- **Validation Rules**:
  - Customer Age verification ($\ge 18$).
  - Account Type validation.
  - Minimum Balance enforcement on account creation (`₹500` for Savings, `₹1000` for Current).
- **Transaction Safety**:
  - Deposits & Withdrawals.
  - Balance protection preventing negative balances / minimum balance violations.
- **Account Security & Status**:
  - Account locking (`Active` / `Inactive` status).
  - 4-digit PIN verification for sensitive transactions.
- **Enterprise Exception Hierarchy** (Java):
  - `AccountException` (Base Exception)
  - `InsufficientBalanceException`
  - `InvalidAmountException`
  - `InactiveAccountException`
  - `InvalidPinException`
  - `MinimumBalanceViolationException`

---

## 📂 Project Structure

```text
step/
├── Account.java                            # Core Java Account Entity Class (With Exceptions)
├── AccountException.java                   # Base Custom Exception Class
├── InsufficientBalanceException.java       # Custom Exception for low balance
├── InvalidAmountException.java             # Custom Exception for zero/negative amounts
├── InactiveAccountException.java           # Custom Exception for closed accounts
├── InvalidPinException.java                # Custom Exception for PIN errors
├── MinimumBalanceViolationException.java   # Custom Exception for minimum balance breach
├── TestAccountExceptions.java              # Java Test Runner with full exception handling
├── AccountEnhanced.py                      # Enhanced Python Account Model
├── TestAccountEnhanced.py                  # Python Test Runner
└── README.md                               # Documentation
```

---

## 🛠️ How to Run

### **Java Version (Activity 5 & 6)**

Compile and execute with UTF-8 encoding:

```bash
javac -encoding UTF-8 *.java
java "-Dfile.encoding=UTF-8" TestAccountExceptions
```

### **Python Version (Activity 3 & 4)**

Execute test suite:

```bash
python TestAccountEnhanced.py
```
