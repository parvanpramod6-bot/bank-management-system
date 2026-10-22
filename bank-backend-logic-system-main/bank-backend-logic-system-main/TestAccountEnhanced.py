import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from AccountEnhanced import Account

def display_account(acc):
    pin_str = "Yes" if acc.hasPin() else "No"
    print(f"Account #{acc.getAccountNumber()} | {acc.getName()} ({acc.getAge()} yrs) | {acc.getAccountType()} | ₹{acc.getBalance()} | {acc.getStatus()} | PIN: {pin_str}")

def main():
    accounts = []

    print("============================================================")
    print("ENHANCED ACCOUNT TEST (BOOLEAN RETURNS)")
    print("============================================================")

    # >>> Test 1: Valid Account Creation
    print(">>> Test 1: Valid Account Creation")
    acc1 = Account(1001, "John Doe", 25, 1000.0, "Savings")
    accounts.append(acc1)
    display_account(acc1)
    print()

    # >>> Test 2: Invalid Age (under 18)
    print(">>> Test 2: Invalid Age (under 18)")
    print("Creating account with age 16")
    acc2 = Account(1002, "Young Kid", 16, 500.0, "Savings")
    accounts.append(acc2)
    print(f"Age auto-corrected to: {acc2.getAge()}")
    display_account(acc2)
    print()

    # >>> Test 3: Invalid Account Type
    print(">>> Test 3: Invalid Account Type")
    print('Creating account with type "Invalid"')
    acc3 = Account(1003, "Test User", 25, 500.0, "Invalid")
    accounts.append(acc3)
    print(f"Account type defaulted to: {acc3.getAccountType()}")
    display_account(acc3)
    print()

    # >>> Test 4: Minimum Balance Enforcement on Creation
    print(">>> Test 4: Minimum Balance Enforcement on Creation")
    print("Creating Savings account with ₹300 (below minimum)")
    acc4 = Account(1004, "Bob Wilson", 25, 300.0, "Savings")
    accounts.append(acc4)
    print(f"Balance auto-corrected to minimum: ₹{acc4.getBalance()}")
    display_account(acc4)
    print()

    # >>> Test 5: Withdrawal with Minimum Balance
    print(">>> Test 5: Withdrawal with Minimum Balance")
    acc5 = Account(1005, "Alice Brown", 30, 1000.0, "Current")
    acc5.setPin(1234)
    accounts.append(acc5)
    print("Initial: ", end="")
    display_account(acc5)

    with_amount1 = 200.0
    if acc5.withdraw(with_amount1, 1234):
        print(f"Withdrawing ₹{with_amount1}: SUCCESS")
        print(f"New balance: ₹{acc5.getBalance()}")
    else:
        print(f"Withdrawing ₹{with_amount1}: FAILED")

    print("After withdrawal: ", end="")
    display_account(acc5)

    with_amount2 = 900.0
    if acc5.withdraw(with_amount2, 1234):
        print(f"Withdrawing ₹{with_amount2} (would leave ₹-100): SUCCESS")
    else:
        print(f"Withdrawing ₹{with_amount2} (would leave ₹-100): FAILED (Minimum balance violation)")
        print(f"Current balance: ₹{acc5.getBalance()}")
    print()

    # >>> Test 6: Account Status Management
    print(">>> Test 6: Account Status Management")
    acc6 = Account(1006, "Charlie Green", 35, 2000.0, "Savings")
    accounts.append(acc6)
    print("Initial: ", end="")
    display_account(acc6)

    if acc6.closeAccount():
        print("Closing account: SUCCESS")
    else:
        print("Closing account: FAILED")

    print("After close: ", end="")
    display_account(acc6)

    dep_amount = 500.0
    if acc6.deposit(dep_amount):
        print(f"Depositing ₹{dep_amount} to closed account: SUCCESS")
    else:
        print(f"Depositing ₹{dep_amount} to closed account: FAILED (Account inactive)")

    if acc6.reopenAccount():
        print("Reopening account: SUCCESS")
    else:
        print("Reopening account: FAILED")

    print("After reopen: ", end="")
    display_account(acc6)
    print()

    # >>> Test 7: PIN Protection
    print(">>> Test 7: PIN Protection")
    acc7 = Account(1007, "Diana Prince", 28, 1500.0, "Savings")
    accounts.append(acc7)

    if acc7.setPin(1234):
        print("Setting PIN 1234: SUCCESS")
    else:
        print("Setting PIN 1234: FAILED")

    with_amt = 200.0
    if acc7.withdraw(with_amt, 1234):
        print(f"Withdrawing ₹{with_amt} with correct PIN (1234): SUCCESS")
        print(f"New balance: ₹{acc7.getBalance()}")
    else:
        print(f"Withdrawing ₹{with_amt} with correct PIN (1234): FAILED")

    if acc7.withdraw(100.0, 9999):
        print("Withdrawing ₹100.0 with incorrect PIN (9999): SUCCESS")
    else:
        print("Withdrawing ₹100.0 with incorrect PIN (9999): FAILED (Incorrect PIN)")

    if acc7.withdraw(100.0, None):
        print("Withdrawing ₹100.0 with PIN not set: SUCCESS")
    else:
        print("Withdrawing ₹100.0 with PIN not set: FAILED (PIN not set)")
    print()

    # >>> Test 8: All Accounts Summary
    print(">>> Test 8: All Accounts Summary")
    for acc in accounts:
        display_account(acc)

    print("============================================================")
    print("ENHANCED TEST COMPLETED!")
    print("============================================================")

if __name__ == "__main__":
    main()
