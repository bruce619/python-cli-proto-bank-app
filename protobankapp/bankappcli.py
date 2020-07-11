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
        self.user_data = []
        self.current_user = {}

    def write_json(self):
        with open('data_file.json', 'w') as json_file:
            json.dump(self.user_data, json_file)

    def read_json(self):
        with open('data_file.json') as json_file:
            self.user_data = json.load(json_file)

    def createaccount(self):
        # Get Current working Directory
        currentDirectory = os.getcwd()
        # # file name
        file_name = r'\data_file.json'
        # total path
        total_path = currentDirectory + file_name
        # check if the json file exists if no, create file
        if os.path.isfile(total_path) and os.access(total_path, os.R_OK):
            # checks if file exists
            print("File exists and is readable")
            # create new account
            print("""
            =========================================
            Welcome to VGG Banking App!!! 
            =========================================
            kindly enter your details
            =========================================
            """)
            print("")
            # opens file for reading and wrinting
            self.read_json()
            email = input("type your email address: ").lower()
            if ("@" in email) and ("." in email):
                if email in ([sub['email'] for sub in self.user_data]):
                    print("User already exist ")
                    self.createaccount()
                else:
                    pins = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
                    password = input("input pin: ")
                    while len(password) == 4:
                        if (password[0] in pins) and (password[1] in pins) and (password[2] in pins) and (password[3] in pins):
                            # initialize the balance to $0.0
                            self.user_data.append(
                                    {

                                        "email": email,
                                        "password": password,
                                        "balance": 0.0,

                                    }
                                    )
                            print("account has been created!!")
                            print("=========================================")
                            self.write_json()
                            print(self.user_data)
                            self.transaction()
                            break
                        else:
                            print("Invalid Input, Input must all be digits")
                            self.createaccount()
                            break
                    else:
                        print("Pin is not valid, please input a 4 digit Pin")
                        self.createaccount()
            else:
                print("Email is not valid, Please try again")
                self.createaccount()
        else:
            print("=============================================================================")
            print("Either file is missing or is not readable, creating file...")
            self.write_json()
            print("=============================================================================")
            print("Successfully created file. Press 1 to create your account ")
            self.createaccount()

    def login_user(self, email, password):
        for i in self.user_data:
            if email == i["email"] and password == i["password"]:
                return i
        return False

    def get_user(self, email):
        for i in self.user_data:
            if email == i["email"]:
                return i
        return False

    def transaction(self):
        # Authenticate user before performing any transaction
        print("""
        =========================================
        Welcome valued customer!!! Perform transactions here 
        =========================================
        """)
        # read from the json file
        self.read_json()

        input_email = input("input email address: ")
        input_password = input("password: ")
        self.current_user = self.login_user(input_email, input_password)

        if self.current_user:
            print("You are in!!!")
            print("Please proceed to select a transaction type")
            print("""
            =========================================
            =========================================
            """)
            # show authenticated user transaction options
            prompt = input("""
            Press 1: Check balance: 
            Press 2: Deposit: 
            Press 3: Withdraw: 
            Press4: Transfer:
            """)
            if prompt == "1":
                self.check_balance()
            elif prompt == "2":
                self.deposit()
            elif prompt == "3":
                self.withdraw()
            elif prompt == '4':
                self.transfer()
            elif prompt == 'q':
                quit()
            else:
                print("Invalid selection, please try again")
                self.transaction()
        else:
            print("Incorrect email or/and Password, Try again")
            retry = input("Press 1: To try again: \nPress 2: create account: ")
            if retry == '1':
                self.transaction()
            elif retry == '2':
                self.createaccount()
            else:
                print("Invalid response")
                quit()

    def check_balance(self):
        # Check user balance
        print("""
        =========================================
        Check your account balance
        =========================================
        Checking your balance....
        =========================================
        """)
        print("\n Net Available Balance=", self.current_user["balance"])
        print("""
        =========================================
        Thank you for banking with us
        =========================================
        """)

        self.transaction()

    def deposit(self):
        # Deposit in user account
        print("""
        =========================================
        Deposit
        =========================================
        """)
        # read from the json file
        deposit_amount = input("Enter amount to be Deposited: ")
        try:
            valid_amount = float(deposit_amount)
            if valid_amount <= 0.0:
                print("Invalid amount, please enter figures only")
                self.deposit()
                return
        except ValueError:
            print("Invalid amount, please enter figures only")
            self.deposit()
            return

        self.current_user["balance"] += valid_amount
        new_balance = self.current_user["balance"]
        print("You have deposited ", valid_amount, "Your new balance is ", new_balance)
        print("""
        =========================================
        Thank you for banking with us
        =========================================
        """)
        self.write_json()
        self.transaction()

    def withdraw(self):
        # withdraw from account
        print("""
        =========================================
        Withdraw
        =========================================
        """)
        # read the json file
        withdraw_amount = (input("Enter amount to be Withdrawn: "))
        while True:
            try:
                valid_withdrawal_amount = float(withdraw_amount)
                if valid_withdrawal_amount <= 0.0:
                    print("Invalid amount, please enter figures only")
                    self.withdraw()
                    return
            except ValueError:
                print("Invalid amount, please enter figures only")
                self.withdraw()
                return

            current_balance = self.current_user["balance"]
            if current_balance < valid_withdrawal_amount:
                print("Insufficient funds, your current balance is", current_balance)
                print("Would you make a DEPOSIT now? y or n")
                option = input()
                if option.lower() == "y":
                    self.deposit()
                elif option.lower() == "n":
                    print("""
                    =========================================
                    Thank you for banking with us
                    =========================================
                    """)
                    quit()
                else:
                    print("Invalid selection")
            else:
                self.current_user["balance"] -= valid_withdrawal_amount
                new_balance = self.current_user["balance"]
                print("You have withdrawn", withdraw_amount, "Your new balance is ", new_balance)
                print("""
                =========================================
                Thank you for banking with us
                =========================================
                """)
                self.write_json()
                self.transaction()

    def transfer(self):
        # transfer to another customer
        print("""
        =========================================
        Transfer
        =========================================
        """)
        transfer_amount = (input("Enter amount to be Transferred: "))
        while True:
            try:
                valid_amount = float(transfer_amount)
                if valid_amount <= 0.0:
                    print("Invalid amount, please enter figures only")
                    self.transfer()
                    return
            except ValueError:
                print("Invalid amount, please enter figures only")
                self.transfer()
                return

            current_balance = self.current_user["balance"]
            # check if there is sufficient balance for the transaction
            if current_balance < valid_amount:
                print("Insufficient funds, your current balance is", current_balance)
                print("Would you make a DEPOSIT now? y or n")
                option = input()
                if option.lower() == "y":
                    self.deposit()
                elif option.lower() == "n":
                    print("""
                    =========================================
                    Thank you for banking with us
                    =========================================
                    """)
                    quit()
                else:
                    print("Invalid selection")
            else:
                recipient = input("Please enter the email of the beneficiary: ")
                receiver = self.get_user(recipient)
                if receiver:
                    self.current_user["balance"] -= valid_amount
                    new_balance = self.current_user['balance']
                    print("You have transferred", valid_amount, "to", recipient, "Your new balance is ", new_balance)
                    print("""
                    =========================================
                    Thank you for banking with us
                    =========================================
                    """)
                    receiver["balance"] += valid_amount
                    self.write_json()
                    self.transaction()
                else:
                    print("===========================================")
                    print("Sorry, ",  recipient, " does not exist, try again")
                    self.transfer()
