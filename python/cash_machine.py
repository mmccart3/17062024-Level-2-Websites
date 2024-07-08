def check_balance(amount):
    global account_balance
    if account_balance - amount >= 0:
        return True
    else:
        return False
    
def dispense_cash(amount, account_number):
    global account_balance
    print(f"Withdrawing {amount} from account number {account_number}.")
    print(f"Your old balance was {account_balance}")
    account_balance = account_balance - amount
    print(f"Your new balance is {account_balance}")

def withdraw_cash(amount, account_number):
    global account_balance
    if check_balance(amount) == False:
        print("Sorry insufficient funds")
    else:
        dispense_cash(amount, account_number)
        
account_balance = 500
withdraw_cash(30, 98765432)
withdraw_cash(60, 98765432)
withdraw_cash(500, 98765432)