def main_menu():
    return input("""
    ============================
    Press 1: Create Account: 
    ============================
    Press 2: Transaction: 
    ============================
    Press q: Quit: 2
    """).lower()

def auth_user_menu():
    return input("""
                Press 1: Check balance: 
                Press 2: Deposit: 
                Press 3: Withdraw: 
                Press 4: Transfer:
                Press 5: See Account
                press q: quit
                """).lower()

def error_selection(msg):
    if(msg=="sel"):
        print("""
                        Invalid selection, please try again
                        """)
    elif(msg=="amo"):
         print("""
                Invalid amount, please enter figures only
                """)
    elif(msg=="email1"):
         print("""
                    User already exist
                    """)
    elif(msg=="val"):
         print("""
                    Invalid Input, Input must all be digits
                     """)
    elif(msg=="pin"):
        print("""
                Pin is not valid, please input a 4 digit Pin
                     """)
    elif(msg=="eval"):
        print("""
                Email is not valid, Please try again
                """)

def re_do_menu():
    input("""
                Press 1: To try again:
                Press 2: create an account:
                """).lower()