class BankAccount:
    def __init__ (self, balance):
        self.balance = balance
    
    def remaining_balance(self):
        print("Your balance is", self.balance)
        
    def withdraw_money(self, amount):
        if amount <= 0:
            print("Amount must be greater than 0")
            return

        elif self.balance >= amount:
            self.balance -= amount
            print("Withdraw", amount, "from your account")
            print("Current Balance:", self.balance)

        else:
            print("Not enough balance!")

    def deposit_money(self, amount):
        if amount <= 0:
            print("Amount must be greater than 0")
            return
        
        print("Current Balance:", self.balance)
        self.balance = self.balance + amount
        print("Updated Balance:", self.balance)

initial_balance  = float(input("What is your initial balance: "))
account = BankAccount(initial_balance)

print("[0] Exit | [1] Withdraw | [2] Deposit | [3] Balance")
while True:
    try:
        choice = int(input("What do you want to do: "))
    except ValueError:
        print("Enter a number only (0-3)")
    continue

    if choice == 0:
        print("\nTransaction Successful!")
        break

    elif choice == 1:
        try:
            amount = float(input("How much money you want to withdraw: "))
            account.withdraw_money(amount)
        except ValueError:
            print("\nEnter a valid number only")
            
    elif choice == 2:
        try:
            amount = float(input("How much money you want to deposit: "))
            account.deposit_money(amount)
        except ValueError:
            print("\nEnter a valid number only")

    elif choice == 3:
        account.remaining_balance()
        
    else:
        print("\nChoice is out of index!")
        continue
        