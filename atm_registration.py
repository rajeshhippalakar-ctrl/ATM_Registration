class ATM:
    bank_name = "ICICI"
    branch = "Hadapsar"

    def __init__(self, customer_name, account_no, balance=2000):
        self.customer_name = customer_name
        self.account_no = account_no
        self.balance = balance

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid amount. Please enter a value greater than 0.")
            return

        self.balance += amount
        print("Amount deposited successfully. Your current balance is:", self.balance)

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount. Please enter a value greater than 0.")
            return

        if amount > self.balance:
            print("Insufficient balance, try again.")
            return

        self.balance -= amount
        print("Withdrawal successful. Your current balance is:", self.balance)


customer1 = ATM(input("Enter your name: "), input("Enter your account number: "))

print("Account has been registered successfully")

while True:
    opt = int(input(
        "Enter your choice: "
        "1 for checking balance, "
        "2 for deposit, "
        "3 for withdrawal, "
        "4 to exit: "
    ))

    if opt == 1:
        print("Your current balance is:", customer1.check_balance())

    elif opt == 2:
        amount = int(input("Enter the amount: "))
        customer1.deposit(amount)

    elif opt == 3:
        amount = int(input("Enter the amount: "))
        customer1.withdraw(amount)

    elif opt == 4:
        print("Thank you for using our services")
        break

    else:
        print("Invalid option, please try again")
