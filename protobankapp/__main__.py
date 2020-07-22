import sys
from .bankappcli import BankApp


def main():
    print('in main')
    args = sys.argv[1:]
    print('count of args :: {}'.format(len(args)))
    for arg in args:
        print('passed argument :: {}'.format(arg))

    bank = BankApp()
    prompt = input("""
    ============================
    Press 1: Create Account: 
    ============================
    Press 2: Transaction: 
    ============================
    Press q: Quit: 
    """).lower()

    while True:
        if prompt == "1":
            bank.create_account()
            break
        elif prompt == '2':
            bank.transaction()
            break
        elif prompt == 'q':
            print("Thank you, Goodbye!!!")
            quit()
            break
        else:
            print("Invalid selection")
            prompt = input("""
            ===========================
            Press 1: Create Account: 
            Press 2: Transaction: 
            Press q: Quit: 
            ===========================
            """)


if __name__ == '__main__':
    main()