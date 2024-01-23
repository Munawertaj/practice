public interface Account {
    public void deposit(int amount);

    public void withdraw(int amount);

    public void transfer(Account toAccount, int amount);

    public int getAccountNumber();

    public int getAmount();
}