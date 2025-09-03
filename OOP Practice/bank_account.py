class bankaccount():
    def __init__(self, account_number, owner_name, balance):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    def deposit_money(self, amount):
        if amount <= 0:
            print("Enter valid amount!")
            return

        self.balance += amount
        print("Amount deposited:", amount)
        print("Current balance:", self.balance)

    def withdraw_money(self, amount):
        if amount <= 0:
            print("Enter valid amount!")
            return

        if self.balance >= amount:
            self.balance -= amount
            print("Amount withdrawn:", amount)
            print("Current balance:", self.balance)
        else:
            print("Insufficient Balance!")

    def check_balance(self):
        print(f"{self.owner_name} your current balance {self.balance}")

client1 = bankaccount(12345, "Client 1", 20000)
client2 = bankaccount(12346, "Clinet 2", 15000)
client3 = bankaccount(12347, "Client 3", 38000)

print("\nClient 1")
client1.deposit_money(2000)
client1.withdraw_money(200)
client1.check_balance()

print("\nClient 2")
client2.deposit_money(100)
client2.withdraw_money(50)
client2.check_balance()

print("\nClient 3")
client3.deposit_money(300)
client3.withdraw_money(100)
client3.check_balance()








# while True:
#     print("[0] Exit | [1] Deposit | [2] Withdraw | [3] Balance")
#     choice = int(input("Which action you want to do: "))
#     if choice == 0:
#         break

#     elif choice == 1:
#         try:
#             amount = float(input("Enter amount: "))
#             client.deposit_money(amount)
#         except ValueError:
#             print("\nEnter a valid number only")

#     elif choice == 2:
#         try:
#             amount = float(input("Enter amount: "))
#             client.withdraw_money(amount)
#         except ValueError:
#             print("\nEnter a valid number only")

#     elif choice == 3:
#         print(f"{client.owner_name} your current balance is {client.balance}")
    
#     else:
#         print("Choice is out of index!")
#         continue