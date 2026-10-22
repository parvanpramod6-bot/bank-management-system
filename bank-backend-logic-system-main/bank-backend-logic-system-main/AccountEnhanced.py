class Account:
    def __init__(self, accountNumber, name, age, initialBalance, accountType):
        self.accountNumber = accountNumber
        self.name = name
        
        # Enhancement 1: Age Validation (min 18)
        if age < 18:
            self.age = 18
        else:
            self.age = age
            
        # Enhancement 2: Account Type Validation ("Savings" or "Current")
        if accountType in ("Savings", "Current"):
            self.accountType = accountType
        else:
            self.accountType = "Savings"
            
        # Enhancement 3: Minimum Balance Rules on Creation
        min_balance = 1000.0 if self.accountType == "Current" else 500.0
        if initialBalance < min_balance:
            self.balance = float(min_balance)
        else:
            self.balance = float(initialBalance)
            
        self.status = "Active"
        self.pin = None

    def _get_min_balance(self):
        return 1000.0 if self.accountType == "Current" else 500.0

    def deposit(self, amount):
        # Enhancement 5: Check if account is active
        if self.status != "Active":
            return False
            
        if amount <= 0:
            return False
            
        self.balance += amount
        return True

    def withdraw(self, amount, pin=None):
        # Enhancement 5: Check if account is active
        if self.status != "Active":
            return False
            
        # Enhancement 6: PIN verification if PIN is set
        if self.hasPin():
            if pin is None or not self.verifyPin(pin):
                return False
                
        if amount <= 0:
            return False
            
        # Enhancement 4: Minimum balance enforcement after withdrawal (balance must not fall below 0)
        if self.balance - amount < 0:
            return False
            
        self.balance -= amount
        return True

    def getAccountNumber(self):
        return self.accountNumber

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getBalance(self):
        return self.balance

    def getAccountType(self):
        return self.accountType

    def getStatus(self):
        return self.status

    def setName(self, name):
        self.name = name

    def setAge(self, age):
        if age < 18:
            self.age = 18
        else:
            self.age = age

    # Enhancement 5: Account Status Management
    def closeAccount(self):
        if self.status == "Inactive":
            return False
        self.status = "Inactive"
        return True

    def reopenAccount(self):
        if self.status == "Active":
            return False
        self.status = "Active"
        return True

    # Enhancement 6: PIN Protection
    def setPin(self, pin):
        if isinstance(pin, int) and 1000 <= pin <= 9999:
            self.pin = pin
            return True
        return False

    def verifyPin(self, pin):
        if not self.hasPin():
            return False
        return self.pin == pin

    def hasPin(self):
        return self.pin is not None

    # Pythonic aliases for snake_case compatibility
    get_account_number = getAccountNumber
    get_name = getName
    get_age = getAge
    get_balance = getBalance
    get_account_type = getAccountType
    get_status = getStatus
    set_name = setName
    set_age = setAge
    close_account = closeAccount
    reopen_account = reopenAccount
    set_pin = setPin
    verify_pin = verifyPin
    has_pin = hasPin


# Alias AccountEnhanced to Account class for convenience
AccountEnhanced = Account
