public class TestAccount {
    public static void main(String[] args) {
        System.out.println("==================================================");
        System.out.println("GLOBAL DIGITAL BANK - ACCOUNT TEST");
        System.out.println("==================================================");

        // 1. Creating Account
        System.out.println(">>> 1. Creating Account");
        Account acc1 = new Account(1001, "John Doe", 25, 1000.0, "Savings");
        System.out.println("Account created!");
        displayAccount(acc1);
        System.out.println();

        // 2. Deposit Money
        System.out.println(">>> 2. Deposit Money");
        double depAmount1 = 500.0;
        if (acc1.deposit(depAmount1)) {
            System.out.println("Depositing ₹" + depAmount1 + ": SUCCESS");
            System.out.println("New balance: ₹" + acc1.getBalance());
        } else {
            System.out.println("Depositing ₹" + depAmount1 + ": FAILED (Invalid amount)");
        }

        double depAmount2 = -100.0;
        if (acc1.deposit(depAmount2)) {
            System.out.println("Depositing ₹" + depAmount2 + ": SUCCESS");
            System.out.println("New balance: ₹" + acc1.getBalance());
        } else {
            System.out.println("Depositing ₹" + depAmount2 + ": FAILED (Invalid amount)");
        }
        System.out.println();

        // 3. Withdraw Money
        System.out.println(">>> 3. Withdraw Money");
        double withAmount1 = 200.0;
        if (acc1.withdraw(withAmount1)) {
            System.out.println("Withdrawing ₹" + withAmount1 + ": SUCCESS");
            System.out.println("New balance: ₹" + acc1.getBalance());
        } else {
            System.out.println("Withdrawing ₹" + withAmount1 + ": FAILED (Insufficient balance)");
            System.out.println("Current balance: ₹" + acc1.getBalance());
        }

        double withAmount2 = 2000.0;
        if (acc1.withdraw(withAmount2)) {
            System.out.println("Withdrawing ₹" + withAmount2 + ": SUCCESS");
            System.out.println("New balance: ₹" + acc1.getBalance());
        } else {
            System.out.println("Withdrawing ₹" + withAmount2 + ": FAILED (Insufficient balance)");
            System.out.println("Current balance: ₹" + acc1.getBalance());
        }
        System.out.println();

        // 4. Creating Another Account
        System.out.println(">>> 4. Creating Another Account");
        Account acc2 = new Account(1002, "Jane Smith", 30, 2000.0, "Current");
        displayAccount(acc2);
        System.out.println();

        // 5. All Accounts
        System.out.println(">>> 5. All Accounts");
        displayAccount(acc1);
        displayAccount(acc2);

        System.out.println("==================================================");
        System.out.println("TEST COMPLETED!");
        System.out.println("==================================================");
    }

    private static void displayAccount(Account acc) {
        System.out.println("Account #" + acc.getAccountNumber() + " | " + acc.getName() + " (" + acc.getAge() + " yrs) | " + acc.getAccountType() + " | ₹" + acc.getBalance() + " | " + acc.getStatus());
    }
}
