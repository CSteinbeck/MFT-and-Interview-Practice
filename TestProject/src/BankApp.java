import javax.swing.plaf.basic.BasicInternalFrameTitlePane;
import java.util.*;
public class BankApp
{
    public static void main(String[] args)
    {
        BankAccount b = new BankAccount();
        //Scanner Objects to pull info
        Scanner name = new Scanner(System.in);
        Scanner id = new Scanner(System.in);
        Scanner input = new Scanner(System.in);
        Scanner amount = new Scanner(System.in);

        System.out.println("Welcome to Colton's Bank!");
        System.out.println("-------------------------");
        System.out.println("Please enter your name");
        String customerName= name.nextLine();
        System.out.println("Please enter your id");
        String customerID = id.nextLine();
        System.out.println("Hello "+name+"! Please tell us what you want to do");
        System.out.println("1. Deposit");
        System.out.println("2. Withdrawl");
        System.out.println("3. Account Amount");
        System.out.println("4. Exit");
        String num= input.nextLine();


        if(num =="1" ){
            System.out.println("Please enter the amount you would like to take out:");
            int amountOut = amount.nextInt();
            b.deposit(amountOut);
        }
    }

    class BankAccount {
       public int balance =0;
        public int previousTransaction=0;

        void deposit(int amount) {
            if (amount == 0) {
                System.out.println("There is no amount that is added");
            } else {
                balance += amount;
                previousTransaction = amount;
                System.out.println("The new balance is " + balance);
            }
        }

        //Withrdrawl method to pull money about the account
        void withdrawl(int amount) {
            if (amount > balance) {
                System.out.println("This amount is greater than the balance.");
            } else {
                balance -= amount;
                System.out.println("The new balance is " + balance);
            }
        }

    }
}

