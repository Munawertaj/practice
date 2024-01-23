
public class Saving implements Account {
    private int accountNumber;
    private int balance;

    public Saving(int accountNumber, int amount) {
        this.accountNumber = accountNumber;
        this.balance = amount;
        System.out.println("Saving account created successfully");
    }

    @Override
    public void deposit(int amount) {
        balance += amount;
        System.out.println("Successfully deposited $" + amount);
    }

    @Override
    public void withdraw(int amount) {
        if (balance >= amount) {
            balance -= amount;
            System.out.println("Successfully withdrawn $" + amount);

        } else {
            System.out.println("Insufficient Balance!!!");
        }
    }

    @Override
    public void transfer(Account toAccount, int amount) {
        this.withdraw(amount);
        toAccount.deposit(amount);
    }

    @Override
    public int getAccountNumber() {
        return accountNumber;
    }

    public int getAmount() {
        return balance;
    }
}
