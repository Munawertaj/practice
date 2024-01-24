import java.util.Hashtable;

public class BankService {
    private Hashtable<Integer, Account> bankAccounts;
    private int accountNumber;

    public BankService() {
        bankAccounts = new Hashtable<Integer, Account>();
        accountNumber = 0;
    }

    public int createNewAccount(String type, int initialAmount) {
        Account newAccount = null;
        accountNumber += 1;

        switch (type.toLowerCase()) {
            case "chequing":
                newAccount = new Chequing(accountNumber, initialAmount);
                break;
            case "saving":
                newAccount = new Saving(accountNumber, initialAmount);
                break;
            case "investment":
                newAccount = new Investment(accountNumber, initialAmount);
                break;
            default:
                System.out.println("Invalid Account type");
                break;
        }

        if (newAccount != null) {
            bankAccounts.put(newAccount.getAccountNumber(), newAccount);
            return newAccount.getAccountNumber();
        }

        return -1;
    }

    public void transferMoney(int to, int from, int amount) {
        Account toAccount = this.bankAccounts.get(to);
        Account fromAccount = this.bankAccounts.get(from);

        if (toAccount != null && fromAccount != null) {
            fromAccount.transfer(toAccount, amount);
        } else {
            System.out.println("Invalid account numbers.");
        }
    }

    public void withdraw(int accountNumber, int amount) {
        Account account = this.bankAccounts.get(accountNumber);
        account.withdraw(amount);
    }

    public void deposit(int accountNumber, int amount) {
        Account account = this.bankAccounts.get(accountNumber);
        account.deposit(amount);
    }

    public int getAmount(int accountNumber) {
        Account account = this.bankAccounts.get(accountNumber);
        int currentBalance = account.getAmount();
        return currentBalance;
    }
}
