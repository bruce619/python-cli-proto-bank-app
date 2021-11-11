import sys

from bankappcli import BankApp
from card import main_menu


def main():
    print('in main')
    args = sys.argv[1:]
    print('count of args :: {}'.format(len(args)))
    for arg in args:
        print('passed argument :: {}'.format(arg))

    bank = BankApp()
    prompt = main_menu()

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
        elif prompt == "5":
            bank.list_registered_account()
        else:
            print("Invalid selection")
            prompt = main_menu()
            


if __name__ == '__main__':
    main()
