from time import sleep
def grind_coffee_beans():
    print("Start grinding coffee")
    sleep(2)
    print("Still grinding")
    sleep(2)
    print("still grinding")
    sleep(2)
    print("coffee ground")

def check_balance(amount):
    global account_balance
    if account_balance - amount >= 0:
        return True
    else:
        return False

def withdraw_cash(amount, account_number):
    global account_balance
    if check_balance(amount) == False:
        print("Sorry insufficient funds")
    else:
        print(f"Withdrawing {amount} from account number {account_number}.")
        print(f"Your old balance was {account_balance}")
        account_balance = account_balance - amount
        print(f"Your new balance is {account_balance}")

def ticket_price():
    age = int(input("whatis your age? ").strip())
    if age <= 17:
        print("£8")
    elif age <= 59:
        print("£10.95")
    else:
        print("£7.95")
        
def my_function():
    answer = 7 * 5
    print(f"Inside the function the variable has this value {answer}")
    
answer = 9 * 10
my_function()    
print(f"Outside the function the variable has this value {answer}")    
    
    
        
# grind_coffee_beans()
# grind_coffee_beans()
# grind_coffee_beans()

account_balance = 500
withdraw_cash(30, 98765432)
withdraw_cash(60, 98765432)
withdraw_cash(500, 98765432)
# withdraw_cash(200, 78945623)

# ticket_price()