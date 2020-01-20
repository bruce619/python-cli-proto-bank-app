import json


class BankApp:
    """A simple command line bank app

        Functions:
            Create Account: Allows users to create an account
                Attributes:
                    --email: request for user email
                    --password: request for user password

            Transaction: Allows verified users to perform bank transactions
                Attributes:
                    --check balance: Allows users to check account balance
                    --deposit: Allows users to deposit into their account
                    --withdrawal: Allows users to withdraw from their account
                    --transfer: allows users to transfers to another users

        """

    def __init__(self):
        self.users = {
            'example@email.com': {'password': '123abc', 'balance': 0.00}
        }
        self.balance = 0

    def createaccount(self):
        # create new account
        print("=========================================")
        print("Welcome to VGG Banking App!!! \n kindly enter your details ")
        print("=========================================\n=========================================")
        email = input("type your email address: ").lower()
        if ("@" in email) and ("." in email):
            if email in self.users.keys():
                print("User already exist ")
            else:
                password =  input("create password: ")
                # initialize the balance to $0.0
                self.balance = 0.0
                self.users[email] = {"password": password, "balance": self.balance}
                print("account has been created!!")
                print("=========================================")
                print(self.users)
                with open('mydata.json', 'w') as f:
                    json.dump(self.users, f)
        else:
            print("Email is not valid, Please try again")
            self.createaccount()

    def transaction(self):
        # Authenticate user before performing any transaction
        print("=========================================")
        print("Welcome valued customer!!! ")
        print("=========================================")
        email = input("input email address: ").lower()
        # check if user exists or not
        # open json and read file
        with open('mydata.json') as json_file:
            data = json.load(json_file)
        if email not in data:
            print("Sorry you are not authorized! \n Kindly create account")
        else:
            password = input("Enter password: ")
            if password == self.users[email]["password"] and self.users[email]["password"] in data:
                print("Welcom!!!")
                print("Please proceed to select a transaction type")
                print("=========================================\n=========================================")
                print("=========================================")
                # show authenticated user transaction options
                prompt = input("Press 1: Check balance: \nPress 2: Deposit: \nPress 3: Withdraw: \nPress4: Transfer: ")
                print("                                         \n                                         ")
                if prompt == "1":
                    self.check_balance(email)
                elif prompt == "2":
                    self.deposit(email)
                elif prompt == "3":
                    self.withdraw(email)
                elif prompt == '4':
                    self.transfer(email)
                else:
                    print("Invalid selection, please try again")

            else:
                print("Incorrect Password, User not Authorized")
                self.createaccount()

    def check_balance(self, email):
        # Check user balance
        print("=========================================")
        print("Check your account balance")
        print("=========================================")
        balance = self.users[email]["balance"]
        print("\n Net Available Balance=", balance)
        print("===============================")
        print("Thank you for banking with us")
        self.transaction()

    def deposit(self, email):
        # Deposit in user account
        print("=========================================")
        print("Deposit")
        print("=========================================")
        deposit_amount = float(input("Enter amount to be Deposited: "))
        while True:
            try:
                valid_amount = float(deposit_amount)
                if valid_amount > 0.0:
                    break
                else:
                    print("Invalid amount, please enter figures only")
                    deposit_amount = input("Please Enter an amount you want to deposit")
            except ValueError:
                print("Invalid amount, please enter figures only")
                deposit_amount = float(input("Enter amount to be Deposited: "))

        current_balance = self.users[email]["balance"]
        self.users[email]["balance"] = current_balance + valid_amount
        new_balance = self.users[email]["balance"]
        print("You have deposited ", valid_amount, "Your new balance is ", new_balance)
        print("===============================")
        print("Thank you for banking with us")
        self.transaction()

    def withdraw(self, email):
        # withdraw from account
        print("=========================================")
        print("Withdraw")
        print("=========================================")
        withdraw_amount = float(input("Enter amount to be Withdrawn: "))
        while True:
            try:
                valid_withdrawal_amount = float(withdraw_amount)
                if valid_withdrawal_amount > 0.0:
                    break
                else:
                    print("Invalid amount, please enter figures only")
                    withdraw_amount = input("Please enter an amount to withdraw")
            except ValueError:
                print("Invalid amount, please enter figures only")
                withdraw_amount = input("Please enter an amount to withdraw")

        current_balance = self.users[email]["balance"]
        if current_balance < valid_withdrawal_amount:
            print("Insufficient funds, your current balance is", current_balance)
            print("Would you make a DEPOSIT now? y or n")
            option = input()
            if option.lower() == "y":
                self.deposit(email)
            elif option.lower() == "n":
                print("===============================")
                print("Thank you for banking with us")
                quit()
            else:
                print("Invalid selection")
        else:
            self.users[email]["balance"] = self.users[email]["balance"]
            new_balance = self.users[email]["balance"]
            print("You have withdrawn", withdraw_amount, "Your new balance is ", new_balance)
            print("===============================")
            print("Thank you for banking with us")
            self.transaction()

    def transfer(self, email):
        # transfer to another customer
        print("=========================================")
        print("Transfer")
        print("=========================================")
        recipient = input("Please enter the email of the beneficiary: ")
        # check if benefiaciary exists or not
        # open json and read file
        with open('mydata.json') as json_file:
            data = json.load(json_file)
        if recipient not in data:
            print("Beneficiary account does not exist, Please try again")
            self.transfer(email)
        transfer_amount = float(input("Enter amount to be Transferred: "))
        while True:
            try:
                valid_amount = float(transfer_amount)
                if valid_amount > 0.0:
                    break
                else:
                    print("Invalid amount, please enter figures only")
                    transfer_amount = input("Please enter the amount to transfer")
            except ValueError:
                print("Invalid amount, please enter figures only")
                transfer_amount = input("Enter amount to be transferRED: ")
        current_balance = self.users[email]["balance"]
        # check if there is sufficient balance for the transaction
        if current_balance < valid_amount:
            print("Insufficient funds, your current balance is", current_balance)
            print("Would you make a DEPOSIT now? y or n")
            option = input()
            if option.lower() == "y":
                self.deposit(email)
            elif option.lower() == "n":
                print("===============================")
                print("Thank you for banking with us")
                quit()
            else:
                print("Invalid selection")
        else:
            self.users[email]["balance"] = current_balance - valid_amount
            new_balance = self.users[email]["balance"]
            recipient_balance = self.users[recipient]["balance"]
            self.users[recipient]["balance"] = recipient_balance + valid_amount
            print("You have transferred", valid_amount, "to", recipient, "Your new balance is ", new_balance)
            print("===============================")
            print("Thank you for banking with us")
            self.transaction()



B = BankApp()


prompt = input("Press 1: Create Account \nPress 2: Transaction \nPress q: to quit ")
while True:
    if prompt == "1" or prompt == "2" or prompt == "q":
        break
    else:
        print("Invalid selection")
        prompt = input("Press 1: Create Account \nPress 2: Transaction \nPress q to quit ")
if prompt == "1":
    B.createaccount()
    B.transaction()
elif prompt == "2":
    BankApp()
    B.transaction()
elif prompt == "q":
    print("Thank you, Goodbye!!!")
    quit()

if __name__ == '__main__':
    BankApp()


