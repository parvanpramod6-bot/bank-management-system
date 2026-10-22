from AccountEnhanced import Account

def test_enhancement_1_age_validation():
    print("Testing Enhancement 1: Age Validation")
    acc = Account(1, "Underage Kid", 15, 1000, "Savings")
    assert acc.getAge() == 18, f"Expected age 18, got {acc.getAge()}"
    
    acc2 = Account(2, "Adult", 25, 1000, "Savings")
    assert acc2.getAge() == 25, f"Expected age 25, got {acc2.getAge()}"
    print("-> Age Validation Passed!")

def test_enhancement_2_type_validation():
    print("Testing Enhancement 2: Account Type Validation")
    acc = Account(1, "User", 20, 1000, "InvalidType")
    assert acc.getAccountType() == "Savings", f"Expected Savings, got {acc.getAccountType()}"
    
    acc2 = Account(2, "User", 20, 2000, "Current")
    assert acc2.getAccountType() == "Current", f"Expected Current, got {acc2.getAccountType()}"
    print("-> Account Type Validation Passed!")

def test_enhancement_3_min_balance_creation():
    print("Testing Enhancement 3: Minimum Balance Rules on Creation")
    acc_sav = Account(1, "Savings User", 20, 200, "Savings")
    assert acc_sav.getBalance() == 500.0, f"Expected 500.0, got {acc_sav.getBalance()}"
    
    acc_curr = Account(2, "Current User", 20, 300, "Current")
    assert acc_curr.getBalance() == 1000.0, f"Expected 1000.0, got {acc_curr.getBalance()}"
    print("-> Minimum Balance Rules on Creation Passed!")

def test_enhancement_4_min_balance_withdrawal():
    print("Testing Enhancement 4: Minimum Balance Enforcement on Withdrawal")
    acc = Account(1, "Savings User", 20, 1000, "Savings") # min bal 500
    # Trying to withdraw 600 leaves balance 400 (below 500 min) -> should fail
    assert acc.withdraw(600) == False, "Expected False for withdrawal dropping below min balance"
    assert acc.getBalance() == 1000.0
    
    # Withdrawing 400 leaves balance 600 (above 500 min) -> should succeed
    assert acc.withdraw(400) == True
    assert acc.getBalance() == 600.0
    print("-> Minimum Balance Enforcement on Withdrawal Passed!")

def test_enhancement_5_status_management():
    print("Testing Enhancement 5: Account Status Management")
    acc = Account(1, "User", 20, 1000, "Savings")
    assert acc.getStatus() == "Active"
    
    assert acc.closeAccount() == True
    assert acc.getStatus() == "Inactive"
    assert acc.closeAccount() == False # Already inactive
    
    # Deposit & withdraw fail when inactive
    assert acc.deposit(500) == False
    assert acc.withdraw(100) == False
    
    assert acc.reopenAccount() == True
    assert acc.getStatus() == "Active"
    assert acc.reopenAccount() == False # Already active
    
    assert acc.deposit(500) == True
    print("-> Status Management Passed!")

def test_enhancement_6_pin_protection():
    print("Testing Enhancement 6: PIN Protection")
    acc = Account(1, "User", 20, 2000, "Savings")
    assert acc.hasPin() == False
    
    # Invalid PINs
    assert acc.setPin(123) == False # 3 digits
    assert acc.setPin(12345) == False # 5 digits
    assert acc.hasPin() == False
    
    # Valid PIN
    assert acc.setPin(1234) == True
    assert acc.hasPin() == True
    assert acc.verifyPin(1234) == True
    assert acc.verifyPin(9999) == False
    
    # Withdrawal with wrong PIN or no PIN should fail
    assert acc.withdraw(200) == False
    assert acc.withdraw(200, 9999) == False
    assert acc.withdraw(200, 1234) == True
    assert acc.getBalance() == 1800.0
    print("-> PIN Protection Passed!")

if __name__ == "__main__":
    test_enhancement_1_age_validation()
    test_enhancement_2_type_validation()
    test_enhancement_3_min_balance_creation()
    test_enhancement_4_min_balance_withdrawal()
    test_enhancement_5_status_management()
    test_enhancement_6_pin_protection()
    print("\nALL ENHANCEMENT TESTS PASSED PERFECTLY!")
