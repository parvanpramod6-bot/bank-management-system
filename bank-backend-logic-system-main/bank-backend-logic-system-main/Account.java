public class Account {
    private int accountNumber;
    private String name;
    private int age;
    private double balance;
    private String accountType;
    private String status;
    private Integer pin;

    public Account(int accountNumber, String name, int age, double initialBalance, String accountType) {
        if (age < 18) {
            throw new IllegalArgumentException("Customer must be at least 18 years old. Provided: " + age);
        }
        if (!"Savings".equals(accountType) && !"Current".equals(accountType)) {
            throw new IllegalArgumentException("Account type must be 'Savings' or 'Current'. Provided: " + accountType);
        }

        double minBalance = "Current".equals(accountType) ? 1000.0 : 500.0;
        if (initialBalance < minBalance) {
            throw new IllegalArgumentException(accountType + " account requires minimum balance of ₹" + minBalance + ". Provided: ₹" + initialBalance);
        }

        this.accountNumber = accountNumber;
        this.name = name;
        this.age = age;
        this.balance = initialBalance;
        this.accountType = accountType;
        this.status = "Active";
        this.pin = null;
    }

    private double getMinimumBalance() {
        return "Current".equals(this.accountType) ? 1000.0 : 500.0;
    }

    public void deposit(double amount) throws InvalidAmountException, InactiveAccountException {
        if ("Inactive".equalsIgnoreCase(this.status)) {
            throw new InactiveAccountException("Account is inactive. Please reopen the account or contact support.");
        }
        if (amount <= 0) {
            throw new InvalidAmountException("Deposit amount must be positive. Provided: ₹" + amount);
        }
        this.balance += amount;
    }

    public void withdraw(double amount, int pin) throws InvalidAmountException, InsufficientBalanceException, MinimumBalanceViolationException, InactiveAccountException, InvalidPinException {
        if ("Inactive".equalsIgnoreCase(this.status)) {
            throw new InactiveAccountException("Account is inactive. Please reopen the account or contact support.");
        }
        if (!hasPin()) {
            throw new InvalidPinException("PIN not set for this account");
        }
        if (this.pin != pin) {
            throw new InvalidPinException("Incorrect PIN");
        }
        if (amount <= 0) {
            throw new InvalidAmountException("Withdrawal amount must be positive. Provided: ₹" + amount);
        }
        if (amount > this.balance) {
            throw new InsufficientBalanceException("Insufficient balance. Available: ₹" + this.balance + ", Requested: ₹" + amount);
        }

        double minBal = getMinimumBalance();
        if (this.balance - amount < minBal) {
            throw new MinimumBalanceViolationException("Cannot withdraw. Minimum balance of ₹" + minBal + " required. Available after withdrawal: ₹" + (this.balance - amount));
        }

        this.balance -= amount;
    }

    public void withdraw(double amount) throws InvalidAmountException, InsufficientBalanceException, MinimumBalanceViolationException, InactiveAccountException, InvalidPinException {
        if ("Inactive".equalsIgnoreCase(this.status)) {
            throw new InactiveAccountException("Account is inactive. Please reopen the account or contact support.");
        }
        if (hasPin()) {
            throw new InvalidPinException("PIN is set for this account. PIN must be provided for withdrawal.");
        }
        if (amount <= 0) {
            throw new InvalidAmountException("Withdrawal amount must be positive. Provided: ₹" + amount);
        }
        if (amount > this.balance) {
            throw new InsufficientBalanceException("Insufficient balance. Available: ₹" + this.balance + ", Requested: ₹" + amount);
        }

        double minBal = getMinimumBalance();
        if (this.balance - amount < minBal) {
            throw new MinimumBalanceViolationException("Cannot withdraw. Minimum balance of ₹" + minBal + " required. Available after withdrawal: ₹" + (this.balance - amount));
        }

        this.balance -= amount;
    }

    public void closeAccount() {
        if ("Inactive".equalsIgnoreCase(this.status)) {
            throw new IllegalStateException("Account is inactive. Please reopen the account or contact support.");
        }
        this.status = "Inactive";
    }

    public void reopenAccount() {
        if ("Active".equalsIgnoreCase(this.status)) {
            throw new IllegalStateException("Account is already active.");
        }
        this.status = "Active";
    }

    public void setPin(int pin) {
        if (pin < 1000 || pin > 9999) {
            throw new IllegalArgumentException("PIN must be a 4-digit number (1000-9999). Provided: " + pin);
        }
        this.pin = pin;
    }

    public boolean verifyPin(int pin) {
        return hasPin() && this.pin == pin;
    }

    public boolean hasPin() {
        return this.pin != null;
    }

    public int getAccountNumber() {
        return accountNumber;
    }

    public String getName() {
        return name;
    }

    public int getAge() {
        return age;
    }

    public double getBalance() {
        return balance;
    }

    public String getAccountType() {
        return accountType;
    }

    public String getStatus() {
        return status;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setAge(int age) {
        if (age < 18) {
            throw new IllegalArgumentException("Customer must be at least 18 years old. Provided: " + age);
        }
        this.age = age;
    }
}
