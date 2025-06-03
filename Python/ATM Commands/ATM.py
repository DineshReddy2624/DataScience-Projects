import time
global balance
global password
global pin
balance = 10000
password = 1234
def check_balance():
    if pin == password:
        print(f"\nYour current balance is: {balance}")
    else:
        print("Wrong pin entered, try again!")

def cash_withdrawal():
    if pin == password:
        withdrawal_amount = int(input("Enter your amount to withdraw: "))
        if withdrawal_amount <= balance:
            new_value=balance- withdrawal_amount
            print(f"{withdrawal_amount} is withdrawn from your account.")
            print(f"Your current balance is: {new_value}")
        else:
            print("Insufficient balance.")
    else:
        print("Wrong pin, try again.")

def cash_deposit():
    if pin == password:
        deposit_amount = int(input("Enter amount to deposit: "))
        new_value=balance+deposit_amount
        print(f"{deposit_amount} is deposited into your account.")
        print(f"Your current balance is: {new_value}")
    else:
        print("Wrong pin, try again.")

def change_pin():
    if pin == password:
        new_password = int(input("Enter your new pin: "))
        old_password = new_password
        print(f"Your updated pin is: {new_password}")
    else:
        print("Wrong pin, try again.")
    return new_password

if __name__ == '__main__':
    print("Welcome to the ATM!")
    time.sleep(2)

    while True:
        print("\nPlease insert your card...")
        time.sleep(2)
        pin = int(input("Enter your pin: "))
        
        if pin == password:
            print("\n1. Check Balance\n2. Cash Withdrawal\n3. Cash Deposit\n4. Change PIN\n5. Eject Card\n")
            option = int(input("Enter your option: "))
            
            match option:
                case 1:
                    check_balance()
                case 2:
                    cash_withdrawal()
                case 3:
                    cash_deposit()
                case 4:
                    change_pin()
                case 5:
                    print("Ejecting card. Thank you for using the ATM!")
                    break
                case _:
                    print("Invalid option, please try again.")
        else:
            print("Wrong pin, try again.")
