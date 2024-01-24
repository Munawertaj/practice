public class Customer {
    public static void main(String[] args) {

        BankService bankService = new BankService();

        int savingAccount = bankService.createNewAccount("saving", 1000);
        int investmentAccount = bankService.createNewAccount("investment", 2000);

        System.out.println("Savings Account Balance is: " + bankService.getAmount(savingAccount));
        System.out.println("Investment Account Balance is: " + bankService.getAmount(investmentAccount));

        bankService.transferMoney(investmentAccount, savingAccount, 500);

        System.out.println("Savings Account Balance is: " + bankService.getAmount(savingAccount));
        System.out.println("Investment Account Balance is: " + bankService.getAmount(investmentAccount));

        bankService.deposit(investmentAccount, 1000);
        bankService.withdraw(savingAccount, 1000);

        System.out.println("Savings Account Balance is: " + bankService.getAmount(savingAccount));
        System.out.println("Investment Account Balance is: " + bankService.getAmount(investmentAccount));

    }
}
