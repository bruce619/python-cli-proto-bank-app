import sys
from .bankappcli import BankApp


def main():
    print('in main')
    args = sys.argv[1:]
    print('count of args :: {}'.format(len(args)))
    for arg in args:
        print('passed argument :: {}'.format(arg))

    bank = BankApp()

    prompt = input("""1: Create Account: 
    2: Transaction: 
    3: Quit: 
    """)
    while True:
        if prompt == "1" or prompt == "2" or prompt == "q":
            break
        else:
            print("Invalid selection")
            prompt = input("""1: Create Account: 
            2: Transaction: 
            3: Quit: 
            """)
    if prompt == "1":
        bank.createaccount()
    elif prompt == "2":
        bank.transaction()
    elif prompt == "q":
        print("Thank you, Goodbye!!!")
        quit()


if __name__ == '__main__':
    main()