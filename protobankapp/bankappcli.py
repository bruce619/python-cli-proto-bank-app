import json
import os
import re
from card import auth_user_menu,error_selection,re_do_menu
from check_email import ama,nums

# Specify the file name
file = 'myfile.json'


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
        with open(os.path.join(os.path.expanduser('~'), 'Documents', file), 'w') as json_file:
            json.dump(self.user_data, json_file, indent=2)

    def read_json(self):
        with open(os.path.join(os.path.expanduser('~'), 'Documents', file), 'r') as json_file:
            self.user_data = json.load(json_file)

    def create_account(self):
        if os.path.isfile(os.path.join(os.path.expanduser('~'), 'Documents', file)):
            # checks if file exists
            print("""
            =========================================
            File exists and is readable
            =========================================
            """)
            # create new account
            print("""
            =========================================
            Welcome to VGG Banking App!!! 
            =========================================
            kindly enter your details
            =========================================
            """)
            # opens file for reading and wrinting
            self.read_json()
            email = input("""
            Create your email address: 
            """).lower()
            if (ama(email)):#USE REGULAR EXPRESSION
                if email in ([sub['email'] for sub in self.user_data]):
                    error_selection("email1")
                    self.create_account()
                else:
                   
                    password = input("""
                    create your 4 digit pin: 
                    """)
                    while len(password) == 4:
                        if (nums(password)):
                            # initialize the balance to $0.0
                            self.user_data.append(
                                    {

                                        "email": email,
                                        "password": password,
                                        "balance": 0.0,

                                    }
                                    )
                            print("""
                            =========================================
                            account has been created!!
                            =========================================
                            """)
                            self.write_json()
                            print(self.user_data)
                            self.transaction()
                            break
                        else:
                            error_selection("val")
                            self.create_account()
                            break
                    else:
                        error_selection("pin")
                        self.create_account()
            else:
                error_selection("eval")
                self.create_account()
        else:
            print("""
            =============================================================================
            Either file is missing or is not readable, creating file...
            =============================================================================
            """)
            self.write_json()
            print("""
            =============================================================================
            Successfully created file. Press 1 to create your account
            =============================================================================
            """)
            self.create_account()

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
        if os.path.isfile(os.path.join(os.path.expanduser('~'), 'Documents', file)):
            # Authenticate user before performing any transaction
            print("""
            =========================================
            Welcome valued customer!!! Perform transactions here 
            =========================================
            """)
            # read from the json file
            self.read_json()

            input_email = input("""
            input email address: 
            """)
            input_password = input("""
            password: 
            """)
            self.current_user = self.login_user(input_email, input_password)

            if self.current_user:
                print("""
                ===========================================
                You are in!!!
                ===========================================
                Please proceed to select a transaction type
                ===========================================
                """)
                # show authenticated user transaction options
                prompt = auth_user_menu()
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
                    error_selection("sel")
                    quit()
            else:
                print("""
                Incorrect email or/and Password, Try again
                """)
                retry = re_do_menu()
                if retry == '1':
                    self.transaction()
                elif retry == '2':
                    self.create_account()
                else:
                    print("""
                    Invalid response
                    """)
                    quit()
        else:
            print("""
           =============================================================================
           Either file is missing or is not readable, creating file...
           =============================================================================
           """)
            self.write_json()
            print("""
                   =============================================================================
                   Successfully created file. Press 1 to create your account
                   =============================================================================
                   """)
            self.create_account()

    def check_balance(self):
        # Check user balance
        print("""
        =========================================
        Check your account balance
        =========================================
        Checking your balance....
        =========================================
        """)
        print("""
        Net Available Balance is {}
        """.format(self.current_user["balance"]))
        print("""
        =========================================
        Thank you for banking with us
        =========================================
        """)
        print("""
        =========================================
        Perform another transaction
        =========================================
        """)
        prompt = auth_user_menu()
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
            error_selection("sel")
            quit()

    def deposit(self):
        # Deposit in user account
        print("""
        =========================================
        Deposit
        =========================================
        """)
        # read from the json file
        deposit_amount = input("""
        Enter amount to be Deposited:
        """)
        try:
            valid_amount = float(deposit_amount)
            if valid_amount <= 0.0:
                error_selection("amo")
                self.deposit()
                return
        except ValueError:
            error_selection("amo")
            self.deposit()
            return

        self.current_user["balance"] += valid_amount
        new_balance = self.current_user["balance"]
        print("""
        You have deposited, {}, Your new balance is, {}
        """.format(valid_amount, new_balance))
        print("""
        =========================================
        Thank you for banking with us
        =========================================
        """)
        self.write_json()
        print("""
        =========================================
        Perform another transaction
        =========================================
        """)
        prompt = auth_user_menu()
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
            error_selection("sel")
            quit()

    def withdraw(self):
        # withdraw from account
        print("""
        =========================================
        Withdraw
        =========================================
        """)
        # read the json file
        withdraw_amount = (input("""
        Enter amount to be Withdrawn:
        """))
        while True:
            try:
                valid_withdrawal_amount = float(withdraw_amount)
                if valid_withdrawal_amount <= 0.0:
                    error_selection("amo")
                    self.withdraw()
                    return
            except ValueError:
                error_selection("amo")
                self.withdraw()
                return

            current_balance = self.current_user["balance"]
            if current_balance < valid_withdrawal_amount:
                print("""
                Insufficient funds, your current balance is {}
                """.format(current_balance)
                      )
                print("""
                Would you make a DEPOSIT now? y or n
                """)
                option = input().lower()
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
                print("""
                You have withdrawn {} Your new balance is {}
                """.format(withdraw_amount, new_balance))
                print("""
                =========================================
                Thank you for banking with us
                =========================================
                """)
                self.write_json()
                print("""
                =========================================
                Perform another transaction
                =========================================
                """)
                prompt = auth_user_menu()
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
                    error_selection("sel")
                    quit()

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
                print("""
                Insufficient funds, your current balance is {}
                """.format(current_balance))
                print("""
                Would you make a DEPOSIT now? y or n
                """)
                option = input().lower()
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
                    error_selection("sel")
            else:
                recipient = input("""
                Please enter the email of the beneficiary:
                """)
                receiver = self.get_user(recipient)
                if receiver:
                    self.current_user["balance"] -= valid_amount
                    new_balance = self.current_user['balance']
                    print("""
                    You have transferred {} to {}, Your new balance is {}
                    """.format(valid_amount, recipient, new_balance)
                          )
                    print("""
                    =========================================
                    Thank you for banking with us
                    =========================================
                    """)
                    receiver["balance"] += valid_amount
                    self.write_json()
                    print("""
                    =========================================
                    Perform another transaction
                    =========================================
                    """)
                    prompt = auth_user_menu()
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
                        error_selection("sel")
                        quit()

                else:
                    print("""
                    ===========================================
                    sorry {} does not exist, try again
                    """.format(recipient))
                    print("""
                    =========================================
                    Perform another transaction
                    =========================================
                    """)
                    prompt = auth_user_menu()
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
                        error_selection("sel")
                        quit()
