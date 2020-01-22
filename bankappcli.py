import io
import json
import os

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
        self.balance = 0
        self.user_data = [
                            {
                                "email": "example@gmail.com",
                                "password": "123re",
                                "balance": 0.0
                            }

                    ]

    def createaccount(self):
        # Get Current working Directory
        currentDirectory = os.getcwd()
        # file name
        file_name = r'\data_file'
        # total path
        total_path = currentDirectory + file_name
        # check if the json file exists if no, create file
        if os.path.isfile(total_path) and os.access(total_path, os.R_OK):
            # checks if file exists
            print("File exists and is readable")
            # create new account
            print("=========================================")
            print("Welcome to VGG Banking App!!! \n kindly enter your details ")
            print("=========================================\n=========================================")
            # opens file for reading and wrinting
            with open('data_file.json', 'r') as json_file:
                data = json.load(json_file)
            email = input("type your email address: ").lower()
            if ("@" in email) and ("." in email):
                if email in ([sub['email'] for sub in data]):
                    print("User already exist ")
                    self.createaccount()
                else:
                    password = input("create password: ")
                    # initialize the balance to $0.0
                    self.balance = 0.0
                    data.append(
                            {

                                "email": email,
                                "password": password,
                                "balance": 0.0,

                            }
                            )
                    print("account has been created!!")
                    print("=========================================")
                    with open('data_file.json', 'w') as json_file:
                        json.dump(data, json_file)
                    print(data)
                    self.transaction()
            else:
                print("Email is not valid, Please try again")
                self.createaccount()
        else:
            print("=============================================================================")
            print("Either file is missing or is not readable, creating file...")
            with io.open(os.path.join(currentDirectory, 'data_file.json'), 'w') as json_file:
                json.dump(self.user_data, json_file)
            print("=============================================================================")
            print("Successfully created file. Run app again and press 1 to create your account ")
            self.createaccount()

    def transaction(self):
        # Authenticate user before performing any transaction
        print("=========================================")
        print("Welcome valued customer!!! Perform transactions here ")
        print("=========================================")
        # read from the json file
        with open('data_file.json', 'r') as json_file:
            data = json.load(json_file)
        input_email = input("input email address: ")
        if input_email in ([sub['email'] for sub in data]):
            input_password = input("password: ")
            if input_password in ([sub['password'] for sub in data]):
                print("You are in!!!")
                print("Please proceed to select a transaction type")
                print("=========================================\n=========================================")
                print("=========================================")
                # show authenticated user transaction options
                prompt = input("Press 1: Check balance: \nPress 2: Deposit: \nPress 3: Withdraw: \nPress4: Transfer: ")
                print("                                         \n                                         ")
                if prompt == "1":
                    self.check_balance(input_email)
                elif prompt == "2":
                    self.deposit(input_email, input_password)
                elif prompt == "3":
                    self.withdraw(input_email, input_password)
                elif prompt == '4':
                    self.transfer(input_email, input_password)
                elif prompt == 'q':
                    quit()
                else:
                    print("Invalid selection, please try again")
                    self.transaction()
            else:
                print("Incorrect Password, Try again")
                self.transaction()
        else:
            print("Sorry you are not authorized! \n Kindly create account")
            self.createaccount()

    def check_balance(self, input_email):
        # Check user balance
        print("=========================================")
        print("Check your account balance")
        print("=========================================")
        # read from the json file
        with open('data_file.json', 'r') as json_file:
            data = json.load(json_file)
        if input_email in ([sub['email'] for sub in data]):
            for key, value in enumerate(data):
                email = (value['email'])
                if email == input_email:
                    print("\n Net Available Balance=", value["balance"])
                    print("===============================")
                    print("Thank you for banking with us")
                    self.transaction()

    def deposit(self, input_email, input_password):
        # Deposit in user account
        print("=========================================")
        print("Deposit")
        print("=========================================")
        # read from the json file
        with open('data_file.json', 'r') as json_file:
            data = json.load(json_file)
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
        if input_password in ([sub['password'] for sub in data]):
            for key, value in enumerate(data):
                password = (value['password'])
                if password == input_password:
                    current_balance = value["balance"]
                    value["balance"] = current_balance + valid_amount
                    new_balance = value["balance"]
                    print("You have deposited ", valid_amount, "Your new balance is ", new_balance)
                    print("===============================")
                    print("Thank you for banking with us")
                    data.append(
                        {

                            "email": input_email,
                            "password": input_password,
                            "balance": new_balance,

                        }
                    )
                    with open('data_file.json', 'w') as json_file:
                        json.dump(data, json_file)
                    self.transaction()

    def withdraw(self, input_email, input_password):
        # withdraw from account
        print("=========================================")
        print("Withdraw")
        print("=========================================")
        # read the json file
        with open('data_file.json', 'r') as json_file:
            data = json.load(json_file)
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
        if input_password in ([sub['password'] for sub in data]):
            for key, value in enumerate(data):
                password = (value['password'])
                if password == input_password:
                    current_balance = value["balance"]
                    if current_balance < valid_withdrawal_amount:
                        print("Insufficient funds, your current balance is", current_balance)
                        print("Would you make a DEPOSIT now? y or n")
                        option = input()
                        if option.lower() == "y":
                            self.deposit(input_password)
                        elif option.lower() == "n":
                            print("===============================")
                            print("Thank you for banking with us")
                            quit()
                        else:
                            print("Invalid selection")
                    else:
                        value["balance"] = value["balance"]
                        new_balance = value["balance"]
                        print("You have withdrawn", withdraw_amount, "Your new balance is ", new_balance)
                        print("===============================")
                        print("Thank you for banking with us")
                        data.append(
                            {

                                "email": input_email,
                                "password": input_password,
                                "balance": new_balance,

                            }
                        )
                        with open('data_file.json', 'w') as json_file:
                            json.dump(data, json_file)
                        self.transaction()

    def transfer(self, input_email, input_password):
        # transfer to another customer
        print("=========================================")
        print("Transfer")
        print("=========================================")
        # check if benefiaciary exists or not
        # open json and read file
        with open('data_file.json', 'r') as json_file:
            data = json.load(json_file)
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
                transfer_amount = input("Enter amount to be transferred: ")
        if input_password in ([sub['password'] for sub in data]):
            for key, value in enumerate(data):
                password = (value['password'])
                if password == input_password:
                    current_balance = value["balance"]
                    # check if there is sufficient balance for the transaction
                    if current_balance < valid_amount:
                        print("Insufficient funds, your current balance is", current_balance)
                        print("Would you make a DEPOSIT now? y or n")
                        option = input()
                        if option.lower() == "y":
                            self.deposit(input_password)
                        elif option.lower() == "n":
                            print("===============================")
                            print("Thank you for banking with us")
                            quit()
                        else:
                            print("Invalid selection")
                    else:
                        recipient = input("Please enter the email of the beneficiary: ")
                        if recipient in ([sub['email'] for sub in data]):
                            value["balance"] = value["balance"] - valid_amount
                            new_balance = value['balance']
                            print("You have transferred", valid_amount, "to", recipient, "Your new balance is ", new_balance)
                            print("===============================")
                            print("Thank you for banking with us")
                            data.append(
                                {

                                    "email": input_email,
                                    "password": input_password,
                                    "balance": new_balance,

                                }
                            )
                            with open('data_file.json', 'w') as json_file:
                                json.dump(data, json_file)
                            self.transaction()
                        else:
                            print("===========================================")
                            print("Sorry, ",  recipient, " does not exist, try again")
                            self.transfer()










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
elif prompt == "2":
    B.transaction()
elif prompt == "q":
    print("Thank you, Goodbye!!!")
    quit()

if __name__ == '__main__':
    BankApp()
import io
import json
import os

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
        self.balance = 0
        self.user_data = [
                            {
                                "email": "example@gmail.com",
                                "password": "123re",
                                "balance": 0.0
                            }

                    ]

    def createaccount(self):
        # Get Current working Directory
        currentDirectory = os.getcwd()
        # file name
        file_name = r'\data_file'
        # total path
        total_path = currentDirectory + file_name
        # check if the json file exists if no, create file
        if os.path.isfile(total_path) and os.access(total_path, os.R_OK):
            # checks if file exists
            print("File exists and is readable")
            # create new account
            print("=========================================")
            print("Welcome to VGG Banking App!!! \n kindly enter your details ")
            print("=========================================\n=========================================")
            # opens file for reading and wrinting
            with open('data_file.json', 'r') as json_file:
                data = json.load(json_file)
            email = input("type your email address: ").lower()
            if ("@" in email) and ("." in email):
                if email in ([sub['email'] for sub in data]):
                    print("User already exist ")
                    self.createaccount()
                else:
                    password = input("create password: ")
                    # initialize the balance to $0.0
                    self.balance = 0.0
                    data.append(
                            {

                                "email": email,
                                "password": password,
                                "balance": 0.0,

                            }
                            )
                    print("account has been created!!")
                    print("=========================================")
                    with open('data_file.json', 'w') as json_file:
                        json.dump(data, json_file)
                    print(data)
                    self.transaction()
            else:
                print("Email is not valid, Please try again")
                self.createaccount()
        else:
            print("=============================================================================")
            print("Either file is missing or is not readable, creating file...")
            with io.open(os.path.join(currentDirectory, 'data_file.json'), 'w') as json_file:
                json.dump(self.user_data, json_file)
            print("=============================================================================")
            print("Successfully created file. Run app again and press 1 to create your account ")
            self.createaccount()

    def transaction(self):
        # Authenticate user before performing any transaction
        print("=========================================")
        print("Welcome valued customer!!! Perform transactions here ")
        print("=========================================")
        # read from the json file
        with open('data_file.json', 'r') as json_file:
            data = json.load(json_file)
        input_email = input("input email address: ")
        if input_email in ([sub['email'] for sub in data]):
            input_password = input("password: ")
            if input_password in ([sub['password'] for sub in data]):
                print("You are in!!!")
                print("Please proceed to select a transaction type")
                print("=========================================\n=========================================")
                print("=========================================")
                # show authenticated user transaction options
                prompt = input("Press 1: Check balance: \nPress 2: Deposit: \nPress 3: Withdraw: \nPress4: Transfer: ")
                print("                                         \n                                         ")
                if prompt == "1":
                    self.check_balance(input_password)
                elif prompt == "2":
                    self.deposit(input_email, input_password)
                elif prompt == "3":
                    self.withdraw(input_email, input_password)
                elif prompt == '4':
                    self.transfer(input_email, input_password)
                elif prompt == 'q':
                    quit()
                else:
                    print("Invalid selection, please try again")
                    self.transaction()
            else:
                print("Incorrect Password, Try again")
                self.transaction()
        else:
            print("Sorry you are not authorized! \n Kindly create account")
            self.createaccount()

    def check_balance(self, input_password):
        # Check user balance
        print("=========================================")
        print("Check your account balance")
        print("=========================================")
        # read from the json file
        with open('data_file.json', 'r') as json_file:
            data = json.load(json_file)
        if input_password in ([sub['password'] for sub in data]):
            for key, value in enumerate(data):
                password = (value['password'])
                if password == input_password:
                    print("\n Net Available Balance=", value["balance"])
                    print("===============================")
                    print("Thank you for banking with us")
                    self.transaction()

    def deposit(self, input_email, input_password):
        # Deposit in user account
        print("=========================================")
        print("Deposit")
        print("=========================================")
        # read from the json file
        with open('data_file.json', 'r') as json_file:
            data = json.load(json_file)
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
        if input_password in ([sub['password'] for sub in data]):
            for key, value in enumerate(data):
                password = (value['password'])
                if password == input_password:
                    current_balance = value["balance"]
                    value["balance"] = current_balance + valid_amount
                    new_balance = value["balance"]
                    print("You have deposited ", valid_amount, "Your new balance is ", new_balance)
                    print("===============================")
                    print("Thank you for banking with us")
                    data.append(
                        {

                            "email": input_email,
                            "password": input_password,
                            "balance": new_balance,

                        }
                    )
                    with open('data_file.json', 'w') as json_file:
                        json.dump(data, json_file)
                    self.transaction()

    def withdraw(self, input_email, input_password):
        # withdraw from account
        print("=========================================")
        print("Withdraw")
        print("=========================================")
        # read the json file
        with open('data_file.json', 'r') as json_file:
            data = json.load(json_file)
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
        if input_password in ([sub['password'] for sub in data]):
            for key, value in enumerate(data):
                password = (value['password'])
                if password == input_password:
                    current_balance = value["balance"]
                    if current_balance < valid_withdrawal_amount:
                        print("Insufficient funds, your current balance is", current_balance)
                        print("Would you make a DEPOSIT now? y or n")
                        option = input()
                        if option.lower() == "y":
                            self.deposit(input_password)
                        elif option.lower() == "n":
                            print("===============================")
                            print("Thank you for banking with us")
                            quit()
                        else:
                            print("Invalid selection")
                    else:
                        value["balance"] = value["balance"]
                        new_balance = value["balance"]
                        print("You have withdrawn", withdraw_amount, "Your new balance is ", new_balance)
                        print("===============================")
                        print("Thank you for banking with us")
                        data.append(
                            {

                                "email": input_email,
                                "password": input_password,
                                "balance": new_balance,

                            }
                        )
                        with open('data_file.json', 'w') as json_file:
                            json.dump(data, json_file)
                        self.transaction()

    def transfer(self, input_email, input_password):
        # transfer to another customer
        print("=========================================")
        print("Transfer")
        print("=========================================")
        # check if benefiaciary exists or not
        # open json and read file
        with open('data_file.json', 'r') as json_file:
            data = json.load(json_file)
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
                transfer_amount = input("Enter amount to be transferred: ")
        if input_password in ([sub['password'] for sub in data]):
            for key, value in enumerate(data):
                password = (value['password'])
                if password == input_password:
                    current_balance = value["balance"]
                    # check if there is sufficient balance for the transaction
                    if current_balance < valid_amount:
                        print("Insufficient funds, your current balance is", current_balance)
                        print("Would you make a DEPOSIT now? y or n")
                        option = input()
                        if option.lower() == "y":
                            self.deposit(input_password)
                        elif option.lower() == "n":
                            print("===============================")
                            print("Thank you for banking with us")
                            quit()
                        else:
                            print("Invalid selection")
                    else:
                        recipient = input("Please enter the email of the beneficiary: ")
                        if recipient in ([sub['email'] for sub in data]):
                            value["balance"] = value["balance"] - valid_amount
                            new_balance = value['balance']
                            print("You have transferred", valid_amount, "to", recipient, "Your new balance is ", new_balance)
                            print("===============================")
                            print("Thank you for banking with us")
                            data.append(
                                {

                                    "email": input_email,
                                    "password": input_password,
                                    "balance": new_balance,

                                }
                            )
                            with open('data_file.json', 'w') as json_file:
                                json.dump(data, json_file)
                            self.transaction()
                        else:
                            print("===========================================")
                            print("Sorry, ",  recipient, " does not exist, try again")
                            self.transfer()










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
elif prompt == "2":
    B.transaction()
elif prompt == "q":
    print("Thank you, Goodbye!!!")
    quit()

if __name__ == '__main__':
    BankApp()
