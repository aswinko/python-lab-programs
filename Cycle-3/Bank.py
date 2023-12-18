class Bank:
    def __init__(self, acc_no, acc_name, acc_type, acc_bal):
        self.acc_no = acc_no
        self.acc_name = acc_name
        self.acc_type = acc_type
        self.acc_bal = acc_bal
    def deposit(self, dep_amt):
        self.acc_bal += dep_amt
        print("Current balance : ", self.acc_bal)
    def withdraw(self, withdraw_amt):
        if self.acc_bal < withdraw_amt:
            print("No money!")
        else:
            self.acc_bal -= withdraw_amt
        print("Currentr balance : ", self.acc_bal)
    def display(self):
        print("Account no : ", self.acc_no)
        print("Account name : ", self.acc_name)
        print("Account type : ", self.acc_type)
        print("Account balance : ", self.acc_bal)

acc_no = input("Enter account no : ")
acc_name = input("Enter account name : ")
acc_type = input("Enter account type : ")
acc_bal = 0
obj = Bank(acc_no, acc_name, acc_type, acc_bal)

deposit_amt = int(input("Enter amount to deposit : "))
obj.deposit(deposit_amt)

withdraw_amt = int(input("Enter amount to withdraw : "))
obj.withdraw(withdraw_amt)

obj.display()